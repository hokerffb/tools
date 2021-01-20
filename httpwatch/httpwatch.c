#include <pcap.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/if_ether.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include "h.h"
#include "public.h"
#include "regex.h"

const char* m_szRegexHost = "Host: (\\S+)";
const char* m_szRegexGet = "GET (\\S+)";
regex_t m_regHost, m_regGet;

void OnHttpPacket(ip_header *ih, u_short dport, const u_char *httpdata, int len)
{
	char *pStart=NULL, *pEnd = NULL;
	char szHttpUrl[256]={0};
	int r = 0;
	regmatch_t rmGet[2]={0}, rmHost[2]={0};
	//hex_print(httpdata,512, 0);
	//printf("-------------------------------------------\n");
	//hex_print(httpdata,512, 0);
/*
	printf("http://%d.%d.%d.%d:%d\n",
       ih->daddr.byte1,
       ih->daddr.byte2,
       ih->daddr.byte3,
       ih->daddr.byte4,
       dport);
*/
	//hex_print(httpdata,512, 0);
	/*
	char *pHostStart = strstr(httpdata, "Host: ");
	if (NULL==pHostStart)
	{
		return;	
	}
	char *pHostEnd = strstr(pHostStart, "\r\n");
	if (NULL==pHostEnd)
	{
		return;
	}
	int nHostLen = pHostEnd - pHostStart;
	if (nHostLen>1024)
		nHostLen = 1024;
	char *pBuf = (char *)malloc(nHostLen + 1);
	memset(pBuf, 0, nHostLen+1);
	memcpy(pBuf, pHostStart, nHostLen);
	*/

	/*
	r = regexec(&m_regHost, (const char*)httpdata, (size_t)2, rmHost, 0);
	if (REG_NOMATCH != r)
	{
		sprintf(szHttpUrl, "%s", Substr(httpdata, rmHost[1].rm_so, rmHost[1].rm_eo) );
		printf("%s, ", szHttpUrl);
	}
	else
		printf("HOst no match\n");
		*/

	pStart = strstr((const char*)httpdata, "Host: ");
	if (pStart!=NULL)
	{
		pEnd = strstr((const char*)pStart, "\r\n");
		if (NULL!=pEnd)
		{
			snprintf(szHttpUrl, pEnd-pStart+1-6, "%s", pStart + 6);
		}
		//printf("HOST:\nURL:%s\n", szHttpUrl);
	}

	/*
	r = regexec(&m_regGet, (const char*)httpdata, (size_t)2, rmGet, 0);
	if (REG_NOMATCH != r)
	{
		//hex_print(httpdata, 256, 0); 
		strcat(szHttpUrl, Substr(httpdata, rmGet[1].rm_so, rmGet[1].rm_eo) );
		printf("%s\n", szHttpUrl);
	}
	else
		printf("get no match\n");
	*/

	char szGetBuf[512]={0};
	pStart = strstr((const char*)httpdata, "GET ");
	if (pStart!=NULL)
	{
		pEnd = strstr((const char*)pStart+4, " ");
		if (NULL!=pEnd)
		{
			snprintf(szGetBuf, pEnd-pStart+1-4, "%s", pStart+4);
			strcat(szHttpUrl, szGetBuf );
		}
		//printf("GET\nURL:%s\n", szHttpUrl);
	}

	if (NULL!=szHttpUrl[0])
		printf("%s(%d)\n", szHttpUrl, strlen(szHttpUrl));
}

void OnPacketCaptured(u_char *useless,const struct pcap_pkthdr* pkthdr,const u_char* packet)
{
	struct in_addr addr;
    struct iphdr *ipptr=NULL;
    struct tcphdr *tcpptr=NULL;
	ip_header *ih=NULL;
	tcp_header *th=NULL;
	char *httpdata=NULL, *data=NULL;

	int i=0;
	u_int ip_len=0, th_len=0;
	u_short sport=0,dport=0;

	u_char *ptr=NULL;
	struct ether_header *eptr=NULL; /* net/ethernet.h */

	 /* lets start with the ether header... */
    eptr = (struct ether_header *) packet;

    /* Do a couple of checks to see what packet type we have..*/
    if (ntohs (eptr->ether_type) == ETHERTYPE_IP)
    {
        //printf("Ethernet type hex:%x dec:%d is an IP packet\n",
        //ntohs(eptr->ether_type), ntohs(eptr->ether_type));
	}
	else if (ntohs (eptr->ether_type) == ETHERTYPE_ARP)
    {
       //printf("Ethernet type hex:%x dec:%d is an ARP packet\n",
		//	ntohs(eptr->ether_type),
		//	ntohs(eptr->ether_type));
    }else {
       //printf("Ethernet type %x not IP", ntohs(eptr->ether_type));
       exit(1);
    }
	////////////////////////////////////////////////////
	
    /* retireve the position of the ip header */
    ih = (ip_header *) (packet + 14); //length of ethernet header
	if (ih->proto!=0x6)
	{
		return;
	}
	ipptr = (struct iphdr*)(packet+sizeof(struct ether_header));
	if ((char *)ih!=(char *)ipptr)
		printf("IP Test:%s\n", (char *)ipptr==(char *)ih?"OK":"NO!");

	//printf("proto=%d\n", ih->proto);
    
	/* retireve the position of the udp header */
    ip_len = (ih->ver_ihl & 0xf) * 4;
    th = (tcp_header *) ((u_char*)ih + ip_len);
	th_len = (4*(th->th_lenres)>>4);

	tcpptr = (struct iphdr*)(packet+sizeof(struct ether_header)
			                                    +sizeof(struct iphdr));
	if ((char *)tcpptr!=(char *)th)
		printf("TCP Test:%s\n", (char *)tcpptr==(char *)th?"OK":"NO!");
    
	/* convert from network byte order to host byte order */
	//sport = ntohs( th->th_sport );
	//dport = ntohs( th->th_dport );

	sport = ntohs(tcpptr->source);
    dport = ntohs(tcpptr->dest);
	//printf("s=%d, d=%d\n", sport, dport);
   /* print ip addresses and udp ports */
   /* printf("%d.%d.%d.%d:%d -> %d.%d.%d.%d:%d\n",
       ih->saddr.byte1,
       ih->saddr.byte2,
       ih->saddr.byte3,
       ih->saddr.byte4,
       sport,
       ih->daddr.byte1,
       ih->daddr.byte2,
       ih->daddr.byte3,
       ih->daddr.byte4,
       dport);
*/
	//httpdata = (char *)ih + ip_len + th_len;
	httpdata = (char *)ipptr + ipptr->ihl*4 + tcpptr->doff*4;
	data = (char*)(packet+sizeof(struct ether_header)+sizeof(struct iphdr)
			                                    +sizeof(struct tcphdr));
	//if (httpdata!=data)
	//	printf("data test:%s\n", httpdata==data?"OK":"NO!");

	if (80==dport || 8080==dport)
	{
		//printf("IPh total len is %d, iplen is %d, thlen is %d\n", 
		//		ih->tlen, ip_len, th_len);
		OnHttpPacket(ih, dport, httpdata, 0);
	}

}


int InitHttp(void)
{
	int r = 0;
	r = regcomp(&m_regGet, m_szRegexGet, REG_ICASE | REG_EXTENDED);
	if (r != 0)
	{
		return r;
	}

	r = regcomp(&m_regHost, m_szRegexHost, REG_ICASE | REG_EXTENDED);
	if (r != 0)
	{
		return r;
	}

	return 0;
}


int main(int argc,char **argv)
{ 
	int nRet = 0;
    int i;
    char *dev; 
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t* descr;
    const u_char *packet;
    struct pcap_pkthdr hdr;     /* pcap.h */
    struct ether_header *eptr;  /* net/ethernet.h */
	u_int localnet=0,netmask = 0;
	struct bpf_program fcode;

	printf("OK.\n");
    //if(argc != 2){ fprintf(stdout,"Usage: %s numpackets\n",argv[0]);return 0;}

	nRet = InitHttp();
	if (nRet != 0)
	{
		printf("Init failed.\n");
		return nRet;
	}

    dev = pcap_lookupdev(errbuf);
    if(dev == NULL)
    { printf("%s\n",errbuf); exit(1); }

    descr = pcap_open_live(dev,BUFSIZ,0,0,errbuf);
    if(descr == NULL)
    { printf("pcap_open_live(): %s\n",errbuf); exit(1); }

	if(pcap_lookupnet(dev, &localnet, &netmask, errbuf) < 0)
	{
		localnet=0;
	    netmask=0;
	}
	// filter
	if (pcap_compile(descr, &fcode, "tcp", 1, netmask)<0)
	{
		printf("pcap_compile error.\n");
		return 0;
	}
	if (pcap_setfilter(descr, &fcode) < 0)
	{
		return 0;
	}

    pcap_loop(descr,0,OnPacketCaptured,NULL);

    return 0;
}
