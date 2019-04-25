/*
 * grunt-modify-pics-plugin
 * https://github.com/sneg55/defiprime
 *
 * Copyright (c) 2019 Lex
 * Licensed under the MIT license.
 */

'use strict';

const fs = require('fs');
const request = require('request');
const url = require("url");
const path = require("path")
const http = require('http');

module.exports = function(grunt) {

  grunt.file.defaultEncoding = 'utf8';

  grunt.registerMultiTask('modify_pics_plugin', 
    'Custom plugin for downloading images from URLs and replacing them.', function() {

    var files = [];
    var options = this.options({
      async: true,
      dest: './dest',
      port: 80,
      method: 'GET'
    });
    var done = this.async();

    var downloadNextSync = function() {
      var file = false;
      files.forEach(function (fileObject) {
        if (!fileObject.downloaded && !fileObject.downloading) {
          file = fileObject;
        }
      });
      if (file) {
        file['request'] = createRequest(file);
        file.request.end();
      } else {
        done();
      }
    };

    var downloadFile = function(file, dest) {
      if (typeof file === 'string') {
        var fileUrl = file;
        file = {
          url: fileUrl
        };
      }

      if (!file.dest) {
        file['dest'] = 'images/output_md';
      }
      if (!file.port) {
        file['port'] = options.port;
      }
      if (!file.method) {
        file['method'] = options.method;
      }
      if (!file.method) {
        file['method'] = options.method;
      }
      if (!file.name) {
        file['name'] = dest.replace(/^.*\//, '') + '.png';
      }

      file['downloaded'] = false;
      file['downloading'] = false;
      file['dlprogress'] = 0;
      file['size'] = 0;
      file['filePath'] = path.join(file.dest, file.name);
      file['tmpPath'] = path.join(file.dest,'.' + file.name);

      // Create the destination directory
      var fileDir = path.dirname(file.filePath);
      grunt.file.mkdir(fileDir);

      files.push(file);
    };

    var createRequest = function(file) {
      file['host'] = url.parse(file.url).hostname;
      file['path'] = url.parse(file.url).pathname;

      if (file.overwrite == undefined) {
        file.overwrite = false;
      }
      if (fs.existsSync(file.filePath) && !file.overwrite) {
        return {
          'end':function() {
            file.downloaded = true;
            file.downloading = false;
            downloadNextSync();
        }};
      }

      if (fs.existsSync(file.tmpPath)) {
        fs.unlinkSync(file.tmpPath);
      }

      return http.request(file, function (response) {
        chunkedResponse(file, response);
      });
    };

    var chunkedResponse = function (file, response) {
      file.downloading = true;
      var downloadfile = fs.createWriteStream(file.tmpPath, {'flags': 'w'});

      file['size'] = response.headers['content-length'];

      response.on('end', function () {
        downloadfile.end(function () {
          fs.renameSync(file.tmpPath, file.filePath);
          file.downloaded = true;
          file.downloading = false;
          downloadNextSync();
        });
      });
      response.pipe(downloadfile);
    };
    
    this.files.forEach(function(f) {
      f.src.filter(function(filepath) {
        // Warn on and remove invalid source files (if nonull was set).
        if (!grunt.file.exists(filepath)) {
          grunt.log.warn('Source file "' + filepath + '" not found.');
          return false;
        } else {
          return true;
        }
      }).map(function(filepath) {
        let mdFile = grunt.file.read(filepath);

        var regex = /!\[\]\(\/\/image.*\)/g,
            matches,
            picsUrls = [];

        while (matches = regex.exec(mdFile)) {
          let singleUrl = matches[0].replace(/!\[\]\(|\)/g, '');
          if (!fs.existsSync(f.dest + '/')) {
            fs.mkdirSync(f.dest + '/');
          }
          const fName = (singleUrl.substr(singleUrl.indexOf('http'), singleUrl.length - 1)).replace(/\/\/?|\.|:/g,'')
          const file = f.dest + '/' + encodeURIComponent(fName);
          downloadFile('http:'+singleUrl, file);
          picsUrls.push({ file, origFile: matches[0]});
        }

        picsUrls.forEach(picUrl => {
          mdFile = mdFile.replace(
            picUrl.origFile,
            '![](/images/output_md' + picUrl.file.substr(picUrl.file.lastIndexOf('/'), picUrl.file.length - 1) + '.png)');
        });

        let outFile = f.dest + filepath.substr(filepath.lastIndexOf('/'), filepath.length - 1);

        grunt.file.write(outFile, mdFile)
        grunt.log.writeln('File "' + outFile + '" created.');
      });
    });

    downloadNextSync();
  });

};
