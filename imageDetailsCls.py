class IMAGE_DETAILS_CLS:
    def __init__ (self):
        self.filename= None # or whatever
        self.fullpath = None 
        self.size_in_KB = None
        self.last_mod_dt = None
        self.extn = None
        #self.ImageLength            
        self.GPSINFO  = None               
        #self.ResolutionUnit         
        #self.ExifOffset             
        #self.Make                   
        #self.Model                  
        #self.Software              
        #self.Orientation            
        #self.DateTime              
        #self.YCbCrPositioning       
        #self.Resolution            
        #self.Resolution            
        #self.Resolution            
        #self.2Resolution            
        #self.3YResolution            
    #def printContent(self): 
        print ( '\n filename =' , self.filename, '\n fullpath =' , self.fullpath,'\n size_in_KB =' , self.size_in_KB, '\n  self.last_mod_dt =' ,  self.last_mod_dt , '\n Extension =' , self.extn)
