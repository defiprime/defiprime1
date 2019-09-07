require "nokogiri"

class SidePanelGenerator < Jekyll::Generator

    @@headings = ['h1', 'h2', 'h3', 'h4']

    def generate(site)
        parser = Jekyll::Converters::Markdown.new(site.config) 

        site.posts.docs.each do |page|
            if page.data["category"] == 'blog'

                doc = Nokogiri::HTML(parser.convert(page.content))

                elements = doc.css('h1')
                active_el = 'h1'
                if elements.empty?
                    elements = doc.css('h2')
                    active_el = 'h2'
                end

                page.data["toc_sidepanel"] = elements.map do |h1|
                    to_nav_item(page, h1).tap do |item|
                    item["children"] = subheadings(h1, active_el).map { |h2| to_nav_item(page, h2) }
                    end
                end

            end
        end
    end

  # Converts a heading into a hash of the info for a link
  def to_nav_item(page, heading)
    {
      "title" => heading.text, 
      "url" => [page.url, heading['id']].join("#") 
    }
  end

  # Returns an enumerator of all H2s "belonging" to an H1
  def subheadings(el, tag_name)

    tag_index = @@headings.index(tag_name)

    Enumerator.new do |y|
      next_el = el.next_sibling
      while next_el && next_el.name != tag_name
        if next_el.name == @@headings[tag_index + 1] || next_el.name == @@headings[tag_index + 2]
          y << next_el
        end
        next_el = next_el.next_sibling
      end
    end
  end
end