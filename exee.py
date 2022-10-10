import re

pattern = r'[M|R]:[\\s]([\\w\\s\\.\\-:]+)[\\s]<([\\w\\.\\-\\+]+)@([\\w\\.\\-]+)>'

data = """X86
M:	Simon Glass <sjg@chromium.org>
M:	Bin Meng <bmeng.cn@gmail.com>
S:	Maintained
T:	git https://source.denx.de/u-boot/custodians/u-boot-x86.git
F:	arch/x86/
F:	cmd/x86/

XEN
M:	Anastasiia Lukianenko <vicooodin@gmail.com>
M:	Oleksandr Andrushchenko <oleksandr_andrushchenko@epam.com>
S:	Maintained
F:	arch/arm/cpu/armv8/xen/
F:	arch/arm/include/asm/xen.h
F:	arch/arm/include/asm/xen/
F:	cmd/pvblock.c
F:	drivers/serial/serial_xen.c
F:	drivers/xen/
F:	include/pvblock.h
F:	include/xen/
F:	include/xen.h
F:	lib/sscanf.c
F:	test/lib/sscanf.c

XTENSA
M:	Max Filippov <jcmvbkbc@gmail.com>
S:	Maintained
F:	arch/xtensa/

THE REST
M:	Tom Rini <trini@konsulko.com>
L:	u-boot@lists.denx.de
Q:	http://patchwork.ozlabs.org/project/uboot/list/
S:	Maintained
T:	git https://source.denx.de/u-boot/u-boot.git
F:	configs/tools-only_defconfig
F:	*
F:	*/"""

i = len(data)
j=0
s=0
prematch = 0


while i>0:
    match = re.search(pattern,data)
    if match:
        if s<match.start()+1 or match.groups()!=prematch:
            s=match.start()
            prematch = match.groups()
            print(match)

    j+=1
    i-=1


