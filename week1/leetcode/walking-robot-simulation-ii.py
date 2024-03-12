class Robot:

    def __init__(self, width: int, height: int):
        self.w = width-1
        self.h = height-1
        self.pos = [0,0]
        self.dir = 'East'

    def step(self, num: int) -> None:
        p = (self.w+self.h)*2
        num = num % p
        # print(num)
        if num !=0:
            while num>0:
                if self.pos[0]!=self.w and self.pos[1]==0:
                    self.pos[0]+=1
                    self.dir = 'East'
                elif self.pos[0]==self.w and self.pos[1]!= self.h:
                    self.pos[1] +=1
                    self.dir = 'North' 
                elif self.pos[0]>0 and  self.pos[1]== self.h:
                    self.pos[0]-=1
                    self.dir= 'West'
                elif self.pos[0]== 0 and self.pos[1]>0:
                    self.pos[1]-=1
                    self.dir = 'South'
                
                num-=1
        elif self.dir=="East" and self.pos==[0,0]:
            self.dir ="South"
            

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()