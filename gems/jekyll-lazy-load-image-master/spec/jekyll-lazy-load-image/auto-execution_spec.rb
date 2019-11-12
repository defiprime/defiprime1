# frozen_string_literal: true

RSpec.describe "JekyllLazyLoadImage auto execution" do
  before do
    Jekyll::Hooks.reset_registry
  end

  it "should register jekyll hooks for post_render" do
    load "lib/jekyll-lazy-load-image/auto-execution.rb"
    jekyll_hooks_registry = Jekyll::Hooks.instance_variable_get(:@registry)
    JekyllLazyLoadImage.config.owners.each do |owner|
      expect(jekyll_hooks_registry[owner][:post_render]).not_to be_empty
    end
  end
end
