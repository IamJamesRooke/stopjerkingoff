-- PDF only: center each drawing marked {.illustration} on its own line, with no paragraph indent.
-- The drawings are decorative (empty alt text), so screen readers and the audiobook skip them.
if not FORMAT:match("latex") then return {} end
function Para(p)
  if #p.content == 1 and p.content[1].t == "Image" and p.content[1].classes:includes("illustration") then
    local src = p.content[1].src
    return pandoc.RawBlock("latex",
      "\\begin{center}\\includegraphics[width=0.8\\linewidth]{" .. src .. "}\\end{center}")
  end
end
