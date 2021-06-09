from game.action import Action

import tkinter.messagebox as tk_mb

# TODO: Define the DrawActorsAction class here
class DrawActorsAction:
    def __init__(self,output_service,cast):
        self.output_service = output_service
        self.cast = cast
        

        

        
        


    def execute(self,action):
        self.output_service.clear_screen()
        for group in self.cast.values():
            for actor in group:
                self.output_service.draw_actor(actor)
        self.output_service.flush_buffer()