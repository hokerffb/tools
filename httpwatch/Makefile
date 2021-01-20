#====================================================================
#-- PROGRAM ------: syslog
#-- FILENAME -----: Makefile
#-- DESCRIPTION --: 
#-- COPYRIGHT ----: 2009 pyw <peng_yuwei@venustech.com.cn>
#-- AUTHOR -------: pyw -- 720725-0346 -- [EMAIL PROTECTED]
#-- FILE CREATED -: 2009-01-06 11:32
#-- LAST CHANGED -: 2009-01-06 11:32
#====================================================================

#CC = /usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-gcc
CFLAGS = -g 
#CFLAGS = "-Os -s"
DEFINES = -D_SINGLETEST_
LINUXLOG = -DSYSLOG_USESYSTEM

.PHONY: all
all: 
	echo use 'make x86wrt' or 'make mipsel' to make. 
	export CC=gcc
	$(CC) $(CFLAGS) ./public.c -c -o ./public.o
	$(CC) $(CFLAGS) ./httpwatch.c -l pcap ./public.o -o ./w.o

.PHONY: local
local:
	export CC=gcc
	$(CC) $(CFLAGS) ./public.c -c -o ./public.o
	$(CC) $(CFLAGS) ./httpwatch.c -l pcap ./public.o -o ./w.o

.PHONY: x86
x86:
	export C_INCLUDE_PATH=/usr/local/sbin/openwrtx86/staging_dir_i386/usr/include/
	export LIBRARY_PATH=/usr/local/sbin/openwrtx86/staging_dir_i386/usr/lib/
	export LD_LIBRARY_PATH=/usr/local/sbin/openwrtx86/staging_dir_i386/usr/lib/
	export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin/openwrtx86/staging_dir_i386/usr/bin:/usr/local/sbin/openwrtx86/staging_dir_i386
	export CROSS_COMPILE=yes
	export AR=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-ar
	export AS=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-as
	export LD=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-ld
	export NM=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-nm
	export CC=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-gcc
	export CPP=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-cpp
	export GCC=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-gcc
	export CXX=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-g++
	export RANLIB=/usr/local/sbin/openwrtx86/staging_dir_i386/bin/i386-linux-uclibc-ranlib
	export ac_cv_linux_vers=2.4.30
	export CFLAGS="-Os -s"
	mkdir -p ./x86bin
	$(CC) $(CFLAGS) ./public.c -c -o ./x86bin/public.o
	$(CC) $(CFLAGS) ./httpwatch.c -l pcap ./x86bin/public.o -o ./x86bin/w.o

.PHONY: mipsel
mipsel:
	export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin/openwrt/staging_dir_mipsel/usr/bin:/usr/local/sbin/openwrt/staging_dir_mipsel
	export CROSS_COMPILE=yes
	export AR=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-ar
	export AS=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-as
	export LD=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-ld
	export NM=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-nm
	export CC=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-gcc
	export CPP=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-cpp
	export GCC=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-gcc
	export CXX=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-g++
	export RANLIB=/usr/local/sbin/openwrt/staging_dir_mipsel/bin/mipsel-linux-uclibc-ranlib
	export ac_cv_linux_vers=2.4.30
	export CFLAGS="-Os -s"
	mkdir -p ./mipbin
	$(CC) $(CFLAGS) ./public.c -c -o ./mipbin/public.o
	$(CC) $(CFLAGS) ./httpwatch.c -l pcap ./mipbin/public.o -o ./mipbin/w.o

.PHONY: clean
clean:
	rm -f *.o
	rm -f ./mipbin/*.o

