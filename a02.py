def calculateArea (width,length):
    area= width * length
    return area



def checkTilesFit(plot_width,plot_length,tile_width,tile_length):
    if plot_width <= 0 or plot_length <= 0 or tile_width <= 0 or tile_length <=0:
        return False

    if (plot_width*plot_length)%(tile_length*tile_width) ==0:
        return True
    else:
        return False  

def calculateTiles(plot_width, plot_length,tile_width,tile_length):   
    if type(plot_width)== str or type(plot_length)==str or type(tile_width)==str or type(tile_length)==str:
        return "Invalid Input"

    if plot_width == 0 or plot_length == 0 or tile_width == 0 or tile_length ==0:
        return None
     
    if plot_width < 0 or plot_length < 0 or tile_width < 0 or tile_length < 0:
        return "Not Possible" 
    calculateTiles=(plot_width*plot_length)%(tile_width*tile_length)
    if calculateTiles== 0:
        return (plot_width*plot_length)//(tile_width*tile_length)
    else:
        return "Not Possible"

calculateTiles(2,2,2,2)       