#include <stdio.h>

// Create time: 2008-8
int main(int argc, char* args[])
{
    char p[256] = {0};
    int i = 0;
    int offset = 0;
    int len = 256; // TODO: use file size
    int thisline = 0;

    if (argc < 2)
    {
        printf("usage: cax filename [-a]\nby 0xFF 2008-8\n");
        return 0;
    }
    
    FILE *fp = fopen(args[1], "rb");
    if (NULL == fp) {
        printf("Can not open file.\n");
        return 0;
    }
    const char* line;
    int t = 0;
    do
    {
        t = fread(p, len, 1, fp);
        if (t == 0) {
            break;
        }
        line = p;
        while (offset < len)
        {
            printf("%04X ", offset);
            thisline = len - offset;
            if (thisline > 16) {
                thisline = 16;
            }
            for (i = 0; i < thisline; i++) {
                printf("%02X ", line[i] < 0 ? -line[i] : line[i]);
            }
            for (; i < 16; i++) {
                printf("   ");
            }
            for (i = 0; i < thisline; i++) {
                printf("%c", (line[i] >= 0x20 && line[i] < 0x7f) ? line[i] : '.');
            }
            printf("\n");
            offset += thisline;
            line += thisline;
        }
    } while (0);

    fclose(fp);

    return 0;
}
