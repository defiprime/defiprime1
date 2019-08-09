# https://stackoverflow.com/questions/36758072/how-to-insert-the-last-updated-time-stamp-in-jekyll-page-at-build-time/36769049#36769049

Jekyll::Hooks.register :documents, :pre_render do |doc|

    # get the current post last modified time

    cmd = "git log -1 --format=\"%cd\" -- #{doc.path}"

    modification_time = %x[ #{cmd} ]
  
    # inject modification_time in post's datas.
    doc.data['last-modified-date'] = modification_time
  
end