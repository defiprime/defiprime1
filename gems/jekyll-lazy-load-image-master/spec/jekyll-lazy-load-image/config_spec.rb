# frozen_string_literal: true

RSpec.describe JekyllLazyLoadImage::Config do
  subject(:config) { JekyllLazyLoadImage::Config.new }

  describe "#owners" do
    subject { config.owners }

    context "when nothing has been set" do
      it "should return default value" do
        is_expected.to eq(JekyllLazyLoadImage::Config::DEFAULT_CONTAINERS)
      end
    end

    context "when something is set" do
      let(:owners_param) { :documents }

      it "should return default value" do
        config.owners = owners_param
        is_expected.to eq(Array(owners_param))
      end
    end
  end

  describe "#owners=" do
    context "when passed not allowed value" do
      it "should raise error" do
        expect {
          config.owners = :invalid_owner_value
        }.to raise_error ArgumentError
      end
    end

    context "when passed valid value" do
      let(:owners_param) { %i[posts documents] }

      it "should set value" do
        config.owners = owners_param
        expect(config.owners).to eq(owners_param)
      end
    end
  end
end
