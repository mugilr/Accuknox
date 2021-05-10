#!/bin/python

from bcc import BPF

prog="""
int hook_h(void *ctx){
    bpf_trace_printk(" HEllo!\\n");
    return 0;
}
"""

b = BPF (text=prog)
b.attach_kprobe(event="__x64_sys_clone", fn_name="hook_h")
print("PID MESSAGE")
b.trace_print()
