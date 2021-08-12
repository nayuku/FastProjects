#!/bin/env python3
from sys import argv
from string import ascii_uppercase, ascii_lowercase

base64table = ascii_uppercase + ascii_lowercase + "0123456789+/"


def encode(msg):
  # conv to bin_array
  bin_msg = "".join([dec2bin(ord(ch)) for ch in msg])

  # div by 6 bits
  div_array = []
  while len(bin_msg) % 6 != 0:  # append 0s
    bin_msg += "0"

  for i in range(0, len(bin_msg), 6):
    div_array.append("00" + bin_msg[i:i+6])  # append leading 0s

  # to dec -> to Base64table
  return "".join([base64table[bin2dec(num)] for num in div_array])


def decode(msg):
  bin_msg = "".join([dec2bin(base64table.index(num))[2:] for num in msg])
  div_array = []
  msg_len = len(bin_msg)
  while msg_len % 8 != 0:  # discard last group if has less than 8 bits
    msg_len -= 1
  for i in range(0, msg_len, 8):
    div_array.append(bin_msg[i:i+8])
  return "".join([chr(bin2dec(num)) for num in div_array])


def dec2bin(q):
  res = ""
  while q != 0:
    r = q % 2
    q = q // 2
    res += str(r)
  while len(res) != 8:  # adding 0's to be 8 bit long
    res += "0"
  return res[::-1]


def bin2dec(q):
  res, i = 0, 1
  for d in q[::-1]:
    res += i * int(d)
    i = i << 1
  return res

def main():
  if len(argv) != 3 or argv[1] not in ["-e", "-d"]:
    exit("Usage:\n./base64.py [-e/-d] 'text to encode/decode'")
  if argv[1] == "-e":
    print(encode(argv[2]))
  if argv[1] == "-d":
    print(decode(argv[2]))


if __name__ == "__main__":
  main()
