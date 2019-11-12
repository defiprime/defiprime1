# frozen_string_literal: true

module JekyllLazyLoadImage
  class Config
    ALLOWED_JEKYLL_HOOK_CONTAINERS = %i[documents pages posts site].freeze
    DEFAULT_CONTAINERS = %i[posts].freeze

    def owners
      @owners || DEFAULT_CONTAINERS
    end

    def owners=(value)
      return if value.nil? || value.empty?

      @owners = Array(value).map(&:to_sym).tap do |owners_prospective|
        not_allowed_hooks = ALLOWED_JEKYLL_HOOK_CONTAINERS & owners_prospective
        raise ArgumentError, "The owners option must be #{ALLOWED_JEKYLL_HOOK_CONTAINERS.join(" or ")}." if not_allowed_hooks.size.zero?
      end
    end
  end
end
