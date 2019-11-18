# frozen_string_literal: true

RSpec.describe JekyllLazyLoadImage::Translator do
  subject(:translator) { JekyllLazyLoadImage::Translator.new(document, site_config) }
  let(:site_config) do
    JekyllLazyLoadImage::SiteConfig.new(site_config_params)
  end

  describe "#translate" do
    subject { translator.translate }
    let(:site_config_params) do
      {
        "additional_attrs" => additional_attrs,
        "class_attr_values" => class_attr_values,
        "ignore_selectors" => ignore_selectors,
        "preload_image" => preload_image,
        "src_attr_name" => src_attr_name,
      }
    end
    let(:additional_attrs) {}
    let(:class_attr_values) {}
    let(:ignore_selectors) {}
    let(:preload_image) {}
    let(:src_attr_name) { "data-src" }

    context "when the html document does not include img tag" do
      let(:document) do
        "<!DOCTYPE html><html><body></body></html>"
      end

      it "should return html without changing anything" do
        expect(subject.gsub(/[\r\n]/, "")).to eq(document)
      end
    end

    context "when the html document includes img tag" do
      context "without src attribute" do
        let(:document) do
          "<!DOCTYPE html><html><body><img></body></html>"
        end

        it "should return html without changing anything" do
          expect(subject.gsub(/[\r\n]/, "")).to eq(document)
        end
      end

      context "with src attribute" do
        let(:src_default_value) { "/path/to/image" }
        let(:document) do
          "<!DOCTYPE html><html><body><img src='#{src_default_value}'></body></html>"
        end

        it "should translate src attribute and add a new src attribute" do
          is_expected.to match(/<img.*?([[:blank:]]+#{src_attr_name}=("|')#{src_default_value}("|')).*?>/)
          is_expected.not_to match(/<img.*?([[:blank:]]+src=(".*"|'.*')).*?>/)
        end

        context "site config excluded src_attr_name" do
          context "with additional_attrs" do
            let(:additional_attrs) do
              {
                "data-sizes" => "auto",
                "data-time" => "10ms",
              }
            end

            it "should set additional attributes to img tag" do
              is_expected.to match(/<img.*?([[:blank:]]+#{src_attr_name}=("|')#{src_default_value}("|')).*?>/)
              additional_attrs.each do |key, value|
                is_expected.to match(/<img.*?([[:blank:]]+#{key}=("|')#{value}("|')).*?>/)
              end
            end
          end

          context "with class_attr_values" do
            let(:class_attr_values) { ["lazyload"] }

            it "should set class attribute values to img tag" do
              is_expected.to match(/<img.*?([[:blank:]]+#{src_attr_name}=("|')#{src_default_value}("|')).*?>/)
              is_expected.to match(/<img.*?([[:blank:]]+class=("|')#{class_attr_values.join(" ")}("|')).*?>/)
            end
          end

          context "with ignore_selectors" do
            let(:ignore_selectors) { ".#{ignore_selector_class}" }
            let(:ignore_selector_class) { "ignore-lazy-load-image" }
            let(:document) do
              "<!DOCTYPE html><html><body><img src='#{src_default_value}' class='#{ignore_selector_class}'></body></html>"
            end

            it "should ignore translation" do
              expect(subject.gsub(/[\r\n]/, "")).to eq(document.tr("'", '"'))
            end
          end

          context "with preload_image" do
            let(:preload_image) { "/path/to/preload_image" }

            it "should set preload image value to img tag" do
              is_expected.to match(/<img.*?([[:blank:]]+#{src_attr_name}=("|')#{src_default_value}("|')).*?>/)
              is_expected.to match(/<img.*?([[:blank:]]+src=("|')#{preload_image}("|')).*?>/)
            end
          end
        end
      end
    end
  end
end
