#!/usr/bin/python

prog = """
#define KBUILD_MODNAME "filter"
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/in.h>
#include <linux/tcp.h>

/*
static struct tcphdr *tcp_(struct xdp_md *ctx){
  bpf_trace_printk("got a packet\\n");
  void *data = (void *)(long)ctx->data;
  void *data_end = (void *)(long)ctx->data_end;
  struct ethhdr *eth = data;
  if ((void*)eth + sizeof(*eth) <= data_end) {
    struct iphdr *ip = data + sizeof(*eth);
    if ((void*)ip + sizeof(*ip) <= data_end) {
      if (ip->protocol == IPPROTO_TCP) {
       struct tcphdr *tcp = (void*)ip + sizeof(*ip);
        return tcp;
        }
     }
   }
   return 0;
}
*/

int xdp_drop(struct xdp_md *ctx) {
  bpf_trace_printk("got a packet\\n");
  void *data = (void *)(long)ctx->data;
  void *data_end = (void *)(long)ctx->data_end;

  struct ethhdr *eth = data;
  if ((void*)eth + sizeof(*eth) <= data_end) {
    struct iphdr *ip = data + sizeof(*eth);
    if ((void*)ip + sizeof(*ip) <= data_end) {
      if (ip->protocol == IPPROTO_TCP) {
        struct tcphdr *tcp = (void*)ip + sizeof(*ip);
        
        //struct tcphdr *tcp = tcp_(ctx);
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

int xdp_pass(struct xdp_md *ctx) {
  bpf_trace_printk("got a packet\\n");
  void *data = (void *)(long)ctx->data;
  void *data_end = (void *)(long)ctx->data_end;

  struct ethhdr *eth = data;
  if ((void*)eth + sizeof(*eth) <= data_end) {
    struct iphdr *ip = data + sizeof(*eth);
    if ((void*)ip + sizeof(*ip) <= data_end) {
      if (ip->protocol == IPPROTO_TCP) {
        struct tcphdr *tcp = (void*)ip + sizeof(*ip);
        
        //struct tcphdr *tcp = tcp_(ctx);
        if ((void*)tcp + sizeof(*tcp) <= data_end) {
          if (tcp->source == ntohs(8080)) {
            bpf_trace_printk("tcp port 8080 packet dropped\\n");
            return XDP_PASS;
          }
        }
      }
    }
  }
  return XDP_PASS;
}

int xdp_abort(struct xdp_md *ctx) {
  bpf_trace_printk("got a packet\\n");
  void *data = (void *)(long)ctx->data;
  void *data_end = (void *)(long)ctx->data_end;

  struct ethhdr *eth = data;
  if ((void*)eth + sizeof(*eth) <= data_end) {
    struct iphdr *ip = data + sizeof(*eth);
    if ((void*)ip + sizeof(*ip) <= data_end) {
      if (ip->protocol == IPPROTO_TCP) {
        struct tcphdr *tcp = (void*)ip + sizeof(*ip);
        
        //struct tcphdr *tcp = tcp_(ctx);
        if ((void*)tcp + sizeof(*tcp) <= data_end) {
          if (tcp->source == ntohs(8080)) {
            bpf_trace_printk("tcp port 8080 packet dropped\\n");
            return XDP_ABORTED;
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
fn1 = b.load_func("xdp_drop", BPF.XDP)
fn2 = b.load_func("xdp_pass", BPF.XDP)
fn3 = b.load_func("xdp_abort", BPF.XDP)
#fn = b.load_func("filter", BPF.XDP)
#b.attach_xdp(device, fn, 0)

try:
  while True:
   todo=input("Enter th config:\n1 - DROP \n2 - PASS \n3 - ABORT\n")
   if (todo == '1'):
     b.attach_xdp(device, fn1, 0)
   elif (todo == '2'):
     b.attach_xdp(device, fn2, 0)
   elif (todo == '3'):
     b.attach_xdp(device, fn3, 0)
   
  #b.trace_print()
except KeyboardInterrupt:
  pass

b.remove_xdp(device, 0)
