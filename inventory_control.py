# instant receipt and gradual consumption model

import math
class InventoryControl:
    
    #calculating economic order quantity
    @staticmethod
    def calculate_EOQ(c , d , h):
        EOQ = math.sqrt((2 * c * d) / h)
        return EOQ
    
    
    #calculating total order cost
    @staticmethod
    def calculate_TOC(c , d , EOQ : calculate_EOQ):
        result = c * (d/EOQ)
        return result
    
    
    #calculating total holding cost
    @staticmethod
    def calculate_THC(h , b , EOQ : calculate_EOQ):
        result = h * (b + EOQ/2)
        return result
    
    
    #calculating total inventory cost
    @staticmethod
    def calculate_TIC(c , b , d , h , EOQ : calculate_EOQ):
        THC = InventoryControl.calculate_THC(h, b, EOQ)
        TOC = InventoryControl.calculate_TOC(c , d , EOQ)
        TIC = TOC + THC
        return TIC





























































