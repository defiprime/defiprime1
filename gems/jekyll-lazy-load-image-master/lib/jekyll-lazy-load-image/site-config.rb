# frozen_string_literal: true

module JekyllLazyLoadImage
  class SiteConfig
    CONFIG_KEY = "lazy_load_image"

    def initialize(lazy_load_image_config)
      @lazy_load_image_config = lazy_load_image_config
    end

    def additional_attrs
      config_key = "additional_attrs"
      @additional_attrs ||= (@lazy_load_image_config&.[](config_key) || {}).tap do |attrs|
        raise "#{config_key} must be associative array. But passed #{attrs || "nil"}" unless attrs.is_a?(Hash)
      end
    end

    def class_attr_values
      config_key = "class_attr_values"
      @class_attr_values ||= Array(
        @lazy_load_image_config&.[](config_key)
      ).compact
    end

    def ignore_selectors
      config_key = "ignore_selectors"
      @ignore_selectors ||= Array(
        @lazy_load_image_config&.[](config_key)
      ).map(&:to_s).reject(&:empty?)
    end

    def preload_image
      config_key = "preload_image"
      @preload_image ||= @lazy_load_image_config&.[](config_key).to_s.strip
    end

    def src_attr_name
      config_key = "src_attr_name"
      @src_attr_name ||= @lazy_load_image_config&.[](config_key).to_s.strip.tap do |name|
        raise "You must set #{config_key} config attribute of #{CONFIG_KEY}" if name.empty?
      end
    end
  end
end
