#define KBUILD_MODNAME "filter"

#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/in.h>
#include <linux/tcp.h>

#ifndef SEC
#define SEC(NAME) __attribute__((section(NAME), used))
#endif


SEC("drop")
int filter(struct xdp_md *ctx) {
  bpf_trace_printk("got a packet\n");
  void *data = (void *)(long)ctx->data;
  void *data_end = (void *)(long)ctx->data_end;
  struct ethhdr *eth = data;
  if ((void*)eth + sizeof(*eth) <= data_end) {
    struct iphdr *ip = data + sizeof(*eth);
    if ((void*)ip + sizeof(*ip) <= data_end) {
      if (ip->protocol == IPPROTO_TCP) {
        struct tcphdr *tcp = (void*)ip + sizeof(*ip);
        if ((void*)tcp + sizeof(*tcp) <= data_end) {
          bpf_trace_printk("tcp port: %d\n", ntohs(tcp->source));
          if (tcp->source == ntohs(8080)) {
            bpf_trace_printk("tcp port 8080 packet dropped\n");
            return XDP_DROP;
          }
        }
      }
    }
  }
  return XDP_PASS;
}

