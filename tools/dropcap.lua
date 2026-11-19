-- PDF only: give the first paragraph of each chapter a drop cap (\lettrine) and
-- small capitals for the rest of its first word. Epigraphs (block quotes) are skipped.
if not FORMAT:match("latex") then return {} end

local function dropcap(para)
  local first = para.content[1]
  if not first or first.t ~= "Str" then return false end
  local text = first.text
  local initial, rest = text:match("^([%a])(.*)$")
  if not initial then return false end
  -- the rest of the word, up to the first space, goes into small capitals
  local tail = rest
  local i = 2
  while para.content[i] and para.content[i].t == "Str" do
    tail = tail .. para.content[i].text
    i = i + 1
  end
  -- a first paragraph shorter than the three lines a drop cap needs gets a raised initial
  local opt = ""
  if #pandoc.utils.stringify(para) < 190 then opt = "[lines=1, loversize=0.9, findent=0.08em, nindent=0.05em]" end
  local tex = "\\lettrine" .. opt .. "{" .. initial .. "}{" .. tail:gsub("([%%#&_{}$])", "\\%1") .. "}"
  local new = { pandoc.RawInline("latex", tex) }
  for j = i, #para.content do new[#new + 1] = para.content[j] end
  para.content = new
  return true
end

local function esc(t)
  return (t:gsub("([%%#&_{}$])", "\\%1"))
end

-- Also: start the main matter (arabic page numbers) at the first chapter, and set the
-- running head for every chapter, numbered or not.
function Pandoc(doc)
  local waiting = false
  local started = false
  local out = {}
  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" and block.level == 1 and not started then
      out[#out + 1] = pandoc.RawBlock("latex", "\\mainmatter")
      started = true
    end
    if block.t == "Header" and block.level == 1 then
      local title = esc(pandoc.utils.stringify(block.content))
      if block.classes:includes("unnumbered") then
        -- unnumbered chapters line up with the numbered ones in the contents
        out[#out + 1] = pandoc.RawBlock("latex",
          "\\hypertarget{" .. block.identifier .. "}{%\n\\chapter*{" .. title .. "}\\label{" .. block.identifier .. "}}\n" ..
          "\\addcontentsline{toc}{chapter}{\\protect\\numberline{}" .. title .. "}")
      else
        out[#out + 1] = block
      end
      out[#out + 1] = pandoc.RawBlock("latex", "\\markboth{" .. title .. "}{" .. title .. "}")
      waiting = true
    else
      out[#out + 1] = block
    end
    if block.t == "Header" and block.level == 1 then
    elseif waiting and block.t == "Para" then
      dropcap(block)
      waiting = false
    elseif waiting and block.t ~= "BlockQuote" and block.t ~= "HorizontalRule" and block.t ~= "RawBlock" and block.t ~= "Div" then
      waiting = false
    end
  end
  doc.blocks = out
  return doc
end
