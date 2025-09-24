module Jekyll
  class PageLayoutsGenerator
    def generate(site)
      pages = site.pages.map! do |page|
        if page.data["layout"].is_a?(Array)
          create_layout_views(page)
        else
          page
        end
      end

      pages.flatten!
    end

    private

    def create_layout_views(page)
      page.data["layout"].map do |layout|
        dir = File.dirname(page.relative_path)
        Page.new(page.site, page.site.source, dir, page.name).tap do |new_page|
          new_page.data["layout"] = layout
        end
      end
    end
  end

  class CollectionLayoutsGenerator
    def generate(site)
      site.collections.each do |_, collection|
        docs = collection.docs.map! do |doc|
          if doc.data["layout"].is_a?(Array)
            create_layout_views(site, collection, doc)
          else
            doc
          end
        end

        docs.flatten!
      end
    end

    private

    def create_layout_views(site, collection, doc)
      doc.data["layout"].map do |layout|
        Document.new(doc.path, :site => site, :collection => collection).tap do |new_doc|
          new_doc.read
          new_doc.data["layout"] = layout
        end
      end
    end
  end

  class MultiPostGenerator < Generator
    safe true

    def generate(site)
      PageLayoutsGenerator.new.generate(site)
      CollectionLayoutsGenerator.new.generate(site)
    end
  end
end