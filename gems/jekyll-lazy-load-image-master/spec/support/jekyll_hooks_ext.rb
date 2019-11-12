# frozen_string_literal: true

module Jekyll
  module Hooks
    class << self
      def reset_registry
        registry = @registry.map do |key, value|
          [key, reset_default_value(value)]
        end
        @registry = Hash[registry]
      end

      private

      def reset_default_value(value)
        if value.is_a?(Hash)
          Hash[value.map { |k, v| [k, reset_default_value(v)] }]
        else
          []
        end
      end
    end
  end
end
