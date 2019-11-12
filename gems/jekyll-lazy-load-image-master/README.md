# Jekyll Lazy Load Image [![Build Status](https://travis-ci.org/kenchan0130/jekyll-lazy-load-image.svg?branch=master)](https://travis-ci.org/kenchan0130/jekyll-lazy-load-image) [![Join the chat at https://gitter.im/kenchan0130/jekyll-lazy-load-image](https://badges.gitter.im/kenchan0130/jekyll-lazy-load-image.svg)](https://gitter.im/kenchan0130/jekyll-lazy-load-image?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

_Edit img tag optimized lazy load images for your Jekyll site_

## Usage
### `Gemfile`

Add the following to your site's `Gemfile`:

```ruby
group :jekyll_plugins do
  gem 'jekyll-lazy-load-image', require: 'jekyll-lazy-load-image/auto-execution'
end
```

and run bundle.

### `_config.yml`

Add the following to your site's `_config.yml`:

```yaml
lazy_load_image:
  src_attr_name: data-src # [required] You need to specify the attributes to be saved for lazy loading
  preload_image: /path/to/image # [optional] you can add a data uri or loading image as fallback src
  class_attr_values: # [optional] if you want to add custom class value, please add values
    - lazyload
  ignore_selectors: # [optional] if you want to ignore applying lazy load image, please add selector (css or xpath)
    - ".ignore-lazy-image-load"
    - "/*[@class='ignore-lazy-image-load']"
  additional_attrs: # [optional] if you want to add attributes, please add key value
    "data-size": auto 
```

### Select lazy load library

Select your favorite library and add your site. For example:
  - [lazysizes](https://github.com/aFarkas/lazysizes) [Recommend]
  - [Echo.js](https://github.com/toddmotto/echo)
  - [TADA](https://github.com/fallroot/tada)
  
## Custom
### Customize container

You can change applying jekyll hook container.
This library is `:posts` by default.

See also: https://jekyllrb.com/docs/plugins/#hooks

#### `Gemfile`

Add the following to your site's `Gemfile`:

```ruby
gem 'jekyll-lazy-load-image'
```

#### `_plugins`

Add the following to your site's `_plugins`, for example create `_plugins/lazy-load-image.rb`:

```ruby
JekyllLazyLoadImage.configure do |config|
  config.owners = %i[posts documents]
end

JekyllLazyLoadImage.execute
```

## Development

- Use `bin/setup` to setup your local development environment.
- Use `bin/console` to load a local Pry console with the Gem.

## Testing

- `bundle exec rake spec`

## Contributing

1. Fork the project
2. Create a descriptively named feature branch
3. Add your feature
4. Submit a pull request
