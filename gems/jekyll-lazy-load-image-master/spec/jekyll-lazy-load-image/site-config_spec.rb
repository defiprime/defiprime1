# frozen_string_literal: true

RSpec.describe JekyllLazyLoadImage::SiteConfig do
  subject(:site_config) { JekyllLazyLoadImage::SiteConfig.new(lazy_load_image_config_params) }

  describe "#additional_attrs" do
    subject { site_config.additional_attrs }

    let(:lazy_load_image_config_params) do
      {
        "additional_attrs" => additional_attrs_params,
      }
    end

    context "without additional_attrs config" do
      let(:lazy_load_image_config_params) { {} }

      it "should be empty hash" do
        is_expected.to be_a(Hash) & be_empty
      end
    end

    context "when additional_attrs config" do
      context "with empty string" do
        let(:additional_attrs_params) { "" }

        it "should raise error" do
          expect { site_config.additional_attrs }.to raise_error StandardError
        end
      end

      context "with hash" do
        let(:additional_attrs_params) do
          {
            "data-sizes" => "auto",
          }
        end

        it "should set value" do
          is_expected.to eq(additional_attrs_params)
        end
      end
    end
  end

  describe "#class_attr_values" do
    subject { site_config.class_attr_values }

    let(:lazy_load_image_config_params) do
      {
        "class_attr_values" => class_attr_values_param,
      }
    end

    context "without class_attr_values config" do
      let(:lazy_load_image_config_params) { {} }

      it "should be empty array" do
        is_expected.to be_a(Array) & be_empty
      end
    end

    context "when class_attr_values config" do
      context "with array" do
        let(:class_attr_values_param) do
          %w(lazyload hidden)
        end

        it "should set value" do
          is_expected.to eq(class_attr_values_param)
        end
      end
    end
  end

  describe "#ignore_selectors" do
    subject { site_config.ignore_selectors }
    let(:lazy_load_image_config_params) do
      {
        "ignore_selectors" => ignore_selectors_param,
      }
    end

    context "without ignore_selectors config" do
      let(:lazy_load_image_config_params) { {} }

      it "should be empty array" do
        is_expected.to be_a(Array) & be_empty
      end
    end

    context "when ignore_selectors config" do
      context "with value" do
        let(:ignore_selectors_param) { ".ignore-lazy-load-image" }

        it "should set value" do
          is_expected.to eq(Array(ignore_selectors_param))
        end
      end
    end
  end

  describe "#preload_image" do
    subject { site_config.preload_image }
    let(:lazy_load_image_config_params) do
      {
        "preload_image" => preload_image_param,
      }
    end

    context "without preload_image config" do
      let(:lazy_load_image_config_params) { {} }

      it "should be empty string" do
        is_expected.to be_a(String) & be_empty
      end
    end

    context "when class_attr_values config" do
      context "with value" do
        let(:preload_image_param) { "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" }

        it "should set value" do
          is_expected.to eq(preload_image_param)
        end
      end
    end
  end

  describe "#src_attr_name" do
    subject { site_config.src_attr_name }
    let(:lazy_load_image_config_params) do
      {
        "src_attr_name" => src_attr_name_param,
      }
    end

    context "without preload_image config" do
      let(:lazy_load_image_config_params) { {} }

      it "should be raise error" do
        expect { site_config.src_attr_name }.to raise_error StandardError
      end
    end

    context "when preload_image config" do
      context "with empty string" do
        let(:src_attr_name_param) { "" }

        it "should be raise error" do
          expect { site_config.src_attr_name }.to raise_error StandardError
        end
      end

      context "with value" do
        let(:src_attr_name_param) { "data-src" }

        it "should set value" do
          is_expected.to eq(src_attr_name_param)
        end
      end
    end
  end
end
