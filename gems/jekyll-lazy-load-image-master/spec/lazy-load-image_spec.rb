# frozen_string_literal: true

RSpec.describe JekyllLazyLoadImage do
  def load_hooks
    JekyllLazyLoadImage::LazyHooks.instance_variable_get(:@load_hooks)
  end

  describe ".config" do
    subject { JekyllLazyLoadImage.config }

    it { is_expected.to be_a(JekyllLazyLoadImage::Config) }
  end

  describe ".execute" do
    before do
      Jekyll::Hooks.reset_registry
    end

    it "should register jekyll hooks for post_render" do
      JekyllLazyLoadImage.execute
      jekyll_hooks_registry = Jekyll::Hooks.instance_variable_get(:@registry)
      JekyllLazyLoadImage.config.owners.each do |owner|
        expect(jekyll_hooks_registry[owner][:post_render]).not_to be_empty
      end
    end
  end
end
