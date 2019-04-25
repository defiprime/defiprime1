module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    modify_pics_plugin: {
      './_posts': ['./_posts/*.md']
    }
  })
  grunt.loadNpmTasks('grunt-modify-pics-plugin');
  grunt.registerTask('default', ['modify_pics_plugin']);
}