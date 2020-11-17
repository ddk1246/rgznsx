# coding=utf-8
import map2d
import Axing

if __name__ == '__main__':
    ##构建地图
    mapTest = map2d.map2d()
    mapTest.showMap()
    ##构建A*
    aStar = Axing.Axing(mapTest, Axing.Node(Axing.Point(1, 1)), Axing.Node(Axing.Point(28, 58)))
    print ("A* start:")
    ##开始寻路
    if aStar.start():
        aStar.setMap()
        mapTest.showMap()
    else:
        print ("no way")