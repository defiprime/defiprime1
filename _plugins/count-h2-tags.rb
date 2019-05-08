module Jekyll

    class CountJekyllTags < Liquid::Tag

        def initialize(tag_name, text, tokens)
            super
            @products_counter = 0
            files = Dir["_posts/**/*.md"]
            files.each do |file|
                File.foreach(file) do |line|
                    if line.start_with?('###')
                        @products_counter = @products_counter + 1
                    end
                end
            end
        end
      
        def render(context)
            @products_counter
        end
    end

end

Liquid::Template.register_tag('products', Jekyll::CountJekyllTags)