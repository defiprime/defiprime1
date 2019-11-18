# frozen_string_literal: true

require "jekyll"

require "jekyll-lazy-load-image/version"
require "jekyll-lazy-load-image/config"
require "jekyll-lazy-load-image/site-config"
require "jekyll-lazy-load-image/translator"

module JekyllLazyLoadImage
  HOOK_KEY = :jekyll_lazy_load_image

  class << self
    def configure
      yield(config)
    end

    def config
      @config ||= Config.new
    end

    def execute
      Jekyll::Hooks.register(config.owners, :post_render) do |post|
        site_config = JekyllLazyLoadImage::SiteConfig.new(
          post.site.config[JekyllLazyLoadImage::SiteConfig::CONFIG_KEY]
        )
        auto_lazy_load_image = JekyllLazyLoadImage::Translator.new(post.output, site_config)
        post.output = auto_lazy_load_image.translate
      end
    end
  end
end
