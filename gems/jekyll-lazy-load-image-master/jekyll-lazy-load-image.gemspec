# frozen_string_literal: true

lib = File.expand_path("lib", __dir__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require "jekyll-lazy-load-image/version"

Gem::Specification.new do |spec|
  spec.name          = "jekyll-lazy-load-image"
  spec.version       = JekyllLazyLoadImage::VERSION
  spec.authors       = ["Tadayuki Onishi"]
  spec.email         = ["tt.tanishi100@gmail.com"]
  spec.summary       = "Edit img tag optimized lazy load images for your Jekyll site"
  spec.homepage      = "https://github.com/kenchan0130/jekyll-lazy-load-image"
  spec.license       = "MIT"

  spec.files         = Dir.chdir(File.expand_path(__dir__)) do
    `git ls-files -z`.split("\x0").reject do |f|
      f.match(%r!^(test|spec|features)/!)
    end
  end
  spec.require_paths = ["lib"]

  spec.required_ruby_version = ">= 2.4.0"

  spec.add_dependency "jekyll", ">= 3.8", "< 5.0"
  spec.add_dependency "nokogiri", "~> 1.8"

  spec.add_development_dependency "bundler", "~> 2.0"
end
