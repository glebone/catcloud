import pygame.camera
import pygame.image
import time
import os


#  ^..^ CAT(c) 2014 CATCloud - CloudApp sharing app on PyGTK
# Webcam shooter class based on pygame library
# --------------------------------------------------------
# 14 Jun 2014 glebone@yandex.ru


def do_shoot():
	if not os.path.exists(os.path.expanduser("~") + "/catcloud_scrns"):
		os.makedirs(os.path.expanduser("~") + "/catcloud_scrns")
 	shoot_nam = os.path.expanduser("~") + "/catcloud_scrns" + "/" + str(time.time()).replace(".", "") + ".png"
 	pygame.camera.init()
   	cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
   	cam.start()
   	img = cam.get_image()
   	pygame.image.save(img, shoot_nam)
   	cam.stop()
   	pygame.camera.quit()
   	return shoot_nam

    	