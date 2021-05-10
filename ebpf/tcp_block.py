#!/usr/bin/python

prog = """
#define KBUILD_MODNAME "filter"
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/in.h>
#include <linux/tcp.h>

int filter(struct xdp_md *ctx) {
  bpf_trace_printk("got a packet\\n");
  void *data = (void *)(long)ctx->data;
  void *data_end = (void *)(long)ctx->data_end;
  struct ethhdr *eth = data;
  if ((void*)eth + sizeof(*eth) <= data_end) {
    struct iphdr *ip = data + sizeof(*eth);
    if ((void*)ip + sizeof(*ip) <= data_end) {
      if (ip->protocol == IPPROTO_TCP) {
        struct tcphdr *tcp = (void*)ip + sizeof(*ip);
        if ((void*)tcp + sizeof(*tcp) <= data_end) {
          if (tcp->source == ntohs(8080)) {
            bpf_trace_printk("tcp port 8080 packet dropped\\n");
            return XDP_DROP;
          }
        }
      }
    }
  }
  return XDP_PASS;
}

"""


from bcc import BPF


device = "lo"
b = BPF(text=prog)
fn = b.load_func("filter", BPF.XDP)
b.attach_xdp(device, fn, 0)

try:
  b.trace_print()
except KeyboardInterrupt:
  pass

b.remove_xdp(device, 0)
