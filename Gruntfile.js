module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    modify_pics_plugin: {
      './output_grunt': ['./_posts/*.md']
    }
  })
  grunt.loadNpmTasks('grunt-modify-pics-plugin');
  grunt.registerTask('default', ['modify_pics_plugin']);
}