import plantconvert as fio
from const import OPFS
import openalea.plantgl.all as pgl

def main():
    # fname="coffee"
    fname="simple_plant"
    # fname = "DA1_Average_MAP_90"
    ext = "opf"
    io = fio.io(file="%s%s.%s"%(OPFS, fname, ext))
    io.read()

    io.write("%s.vtp"%(fname))

if __name__ == "__main__":
    main()