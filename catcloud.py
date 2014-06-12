#!/usr/bin/env python
import gtk
import ntpath
from cloudapp.cloud import Cloud
import pyperclip

# custom modules
import getImage

#  ^..^ CAT(c) 2014 CATCloud - CloudApp sharing app on PyGTK
# --------------------------------------------------------
# 09 Jun 2014 glebone@yandex.ru


ntpath.basename("a/b/c")
image_path = ""



def do_post(path, ulabel):
  mycloud = Cloud()
  mycloud.auth('glebone@yandex.ru', '')
  img = mycloud.upload_file(path.get_text() )
  share_url = img["url"]
  print "Successfully upload photo - "
  print share_url
  ulabel.set_text("Image uploaded by url: " + share_url)
  pyperclip.copy(share_url)


def make_box_urlabel(urlabel):

  box = gtk.HBox(True, 1)

  urlabel.set_alignment(0, 0)
  box.pack_start(urlabel, False, False, 0)
  urlabel.show()
  return box


def make_screenshot_box:

  box = gtk.HBox(True, 1)
  return box

def make_gist_box:

  box = gtk.HBox(True, 1)
  return box






def show_window():
  window = gtk.Window(gtk.WINDOW_TOPLEVEL)
  window.set_title("CATCloud")
  #window.connect("delete_event", self.delete_event)
  window.set_border_width(10)
  window.set_icon_from_file("resources/cicon.png")


  box1 = gtk.VBox(False, 0)
  label = gtk.Label("^..^ CATCloud ")
  label.set_alignment(0, 0)
  box1.pack_start(label, False, False, 0)
  label.show()

  separator = gtk.HSeparator()
  box1.pack_start(separator, False, True, 5)
  separator.show()


  imbox = gtk.HBox(False, 0)
  photo_icon = gtk.Image()
  photo_icon.set_from_file("resources/camera.png")
  photo_icon.show()
  button = gtk.Button()
  button.add(photo_icon)
  imlabel = gtk.Label("No image")
  urllabel = gtk.Label("")
  button.connect("clicked", lambda w: getImage.add_image(imlabel))
  imbox.pack_start(button, True, False, 0)
  imbox.pack_end(imlabel, True, False, 0)



  post_icon = gtk.Image()
  post_icon.set_from_file("resources/check_mark.png")
  post_icon.show()
  postbox = gtk.HBox(False, 0)
  post_button = gtk.Button()
  post_button.add(post_icon)
  post_button.connect("clicked", lambda w: do_post(imlabel, urllabel))
  postbox.pack_start(post_button, True, False, 0)
  box1.pack_start(imbox, False, False, 0)
  box2 = make_box_urlabel(urllabel)
  box1.pack_start(box2, False, False, 0)
  box2.show()




  box1.pack_end(postbox, False, False, 0)
  window.add(box1)


  button.show()
  post_button.show()
  imlabel.show()
  postbox.show()
  imbox.show()
  box1.show()
  window.show()



def open_app(data=None):
  show_window()

def close_app(data=None):
  message(data)
  gtk.main_quit()

def make_menu(event_button, event_time, data=None):
  menu = gtk.Menu()
  open_item = gtk.MenuItem("Open App")
  close_item = gtk.MenuItem("Close App")

  #Append the menu items
  menu.append(open_item)
  menu.append(close_item)
  #add callbacks
  open_item.connect_object("activate", open_app, "Open App")
  close_item.connect_object("activate", close_app, "Close App")
  #Show the menu items
  open_item.show()
  close_item.show()

  #Popup the menu
  menu.popup(None, None, None, event_button, event_time)

def on_right_click(data, event_button, event_time):
  #make_menu(event_button, event_time)
  show_window()

def on_left_click(event):
  print "Showww!"
  show_window()


if __name__ == '__main__':
  file = open("resources/cicon.png", "rb")
  binary = file.read()
  loader = gtk.gdk.PixbufLoader("png")
  loader.write(binary)
  loader.close()
  pixbuf = loader.get_pixbuf()
  #icon = gtk.status_icon_new_from_stock(gtk.STOCK_ABOUT)
  icon  = gtk.status_icon_new_from_pixbuf(pixbuf)
  icon.connect('popup-menu', on_right_click)
  icon.connect('activate', on_left_click)
  gtk.main()
