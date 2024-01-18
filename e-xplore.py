#!/usr/bin/env python3
import colorama
from pwn import *
import sys
import triton
from termcolor import *

colorama.init()

if len(sys.argv) < 2:
    print(colored("Usage: ./e-xplore <elf_file>", 'green', 'on_black', ['blink']))
    sys.exit(0)

try:
    elf_file = sys.argv[1]

except FileNotFoundError:
    print(colored(f"Could not find file \"{elf_file}\"", 'red', 'on_black', ['blink']))
    sys.exit(0)

try:
    print(colored(" _____ _  __   ____  _               _ ", 'light_green', 'on_black', ['blink', 'bold']))
    print(colored("| ____| |/ _| | __ )| | ___  ___  __| |", 'light_red', 'on_black', ['blink', 'bold']))
    print(colored("|  _| | | |_  |  _ \| |/ _ \/ _ \/ _` |", 'light_green', 'on_black', ['blink', 'bold']))
    print(colored("| |___| |  _| | |_) | |  __/  __/ (_| |", 'light_red', 'on_black', ['blink', 'bold']))
    print(colored("|_____|_|_|   |____/|_|\___|\___|\__,_|", 'light_green', 'on_black', ['blink', 'bold']))
    elf_addr = ELF(elf_file)
    print(colored(f"{elf_file}", 'light_green', 'on_black', ['bold', 'underline']))
    print(colored(f"Main Found: {hex(elf_addr.symbols['main'])}", 'light_green', 'on_black', ['underline']))
    print(colored(f"File Tell: {hex(elf_addr.file.tell())}", 'light_green', 'on_black'))
    print(colored(f"Key Values: {elf_addr.sym.keys().isdisjoint(elf_addr.sym.keys())}", 'light_green', 'on_black'))
    print(colored(f"Key Mapping: {elf_addr.sym.keys().mapping.values()}", 'light_green', 'on_black'))
    print(colored(f"File Path: {elf_addr}", 'light_green', 'on_black'))

    file_features = triton.compiler.compiler.annotations
    print(colored(f"File Features: {file_features}", 'light_green', 'on_black'))

    print(colored(f"ASLR Enabled: {elf_addr.aslr}", 'light_green', 'on_black'))
except IOError:
    print(colored(f"Could not make {elf_file} bleed.", 'red', 'on_black', ['blink', 'bold', 'underline']))
