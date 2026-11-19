-- EPUB only: a copyright page after the title page, small capitals on the first word
-- of each chapter, a valid publication date, and a single clean title in the metadata.
if not FORMAT:match("epub") then return {} end

local function copyright_page()
  local month = os.date("%B %Y")
  local paras = {
    "*Stop Jerking Off: The Easy Peasy Way to Conquer Lust*",
    "Published anonymously. This edition: " .. month .. ".",
    "The text of this book is released under the Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0). You may copy, share, print, translate and adapt it, for any purpose, as long as you give credit and release your version under the same license.",
    "The structure and method are inspired by *EasyPeasy* by Hackauthor², also released under CC BY-SA 4.0, which is itself based on Allen Carr's Easyway method. This book is not affiliated with or endorsed by either. Full credits are given in the Attribution at the back of the book.",
    "Bible quotations are from the World English Bible, which is in the public domain. Short quotations from other writers remain the property of their authors.",
    "This book is not medical, psychological or legal advice.",
    "The latest edition is at stopjerkingoff.com",
  }
  local blocks = {}
  for _, md in ipairs(paras) do
    for _, b in ipairs(pandoc.read(md, "markdown").blocks) do blocks[#blocks + 1] = b end
  end
  local head = pandoc.Header(1, "Copyright",
    pandoc.Attr("copyright", {"unnumbered", "unlisted", "copyright-heading"}, {{"epub:type", "copyright-page"}}))
  return { head, pandoc.Div(blocks, pandoc.Attr("", {"copyright"})) }
end

local function title_page(meta)
  local title = pandoc.utils.stringify(meta.title)
  local subtitle = pandoc.utils.stringify(meta.subtitle or "")
  local head = pandoc.Header(1, title,
    pandoc.Attr("title-page", {"unnumbered", "unlisted", "book-title"}, {{"epub:type", "titlepage"}}))
  return { head,
    pandoc.Div({ pandoc.Para({ pandoc.Str(subtitle) }) }, pandoc.Attr("", {"book-subtitle"})),
    pandoc.Div({ pandoc.Para({ pandoc.Str("stopjerkingoff.com") }) }, pandoc.Attr("", {"book-site"})) }
end

-- An in-book contents page; reading systems also get the full navigation file.
local function contents(blocks)
  local items = {}
  local n = 0
  for _, b in ipairs(blocks) do
    if b.t == "Header" and b.level == 1 then
      local label = { pandoc.Span({ pandoc.Str("\u{00A0}") }, pandoc.Attr("", {"toc-num"})), pandoc.Space() }
      if not b.classes:includes("unnumbered") then
        n = n + 1
        label = { pandoc.Span({ pandoc.Str(tostring(n)) }, pandoc.Attr("", {"toc-num"})), pandoc.Space() }
      end
      local inl = pandoc.List(label)
      inl:extend(b.content)
      items[#items + 1] = { pandoc.Plain({ pandoc.Link(inl, "#" .. b.identifier) }) }
    end
  end
  local head = pandoc.Header(1, "Contents",
    pandoc.Attr("contents", {"unnumbered", "unlisted"}, {{"epub:type", "toc"}}))
  return { head, pandoc.Div({ pandoc.BulletList(items) }, pandoc.Attr("", {"contents"})) }
end

local function opening(para)
  local first = para.content[1]
  if not first or first.t ~= "Str" then return para end
  local word = { first }
  local i = 2
  while para.content[i] and para.content[i].t == "Str" do
    word[#word + 1] = para.content[i]
    i = i + 1
  end
  local new = { pandoc.SmallCaps(word) }
  for j = i, #para.content do new[#new + 1] = para.content[j] end
  para.content = new
  return pandoc.Div({ para }, pandoc.Attr("", {"opening"}))
end

function Pandoc(doc)
  doc.meta.date = pandoc.MetaString(os.date("%Y-%m-%d"))
  local out = title_page(doc.meta)
  for _, b in ipairs(copyright_page()) do out[#out + 1] = b end
  for _, b in ipairs(contents(doc.blocks)) do out[#out + 1] = b end
  -- one clean title in the store metadata (the title page above shows it in two lines)
  doc.meta.title = pandoc.MetaString(pandoc.utils.stringify(doc.meta.title) .. ": " .. pandoc.utils.stringify(doc.meta.subtitle))
  doc.meta.subtitle = nil
  local waiting = false
  for _, block in ipairs(doc.blocks) do
    if waiting and block.t == "Para" then
      out[#out + 1] = opening(block)
      waiting = false
    else
      if waiting and block.t ~= "BlockQuote" and block.t ~= "HorizontalRule" and block.t ~= "RawBlock" and block.t ~= "Div" then
        waiting = false
      end
      out[#out + 1] = block
    end
    if block.t == "Header" and block.level == 1 then waiting = true end
  end
  doc.blocks = out
  return doc
end
