# Sainsbury-s-Price-Reduction-List
Full list of all possible yellow sticker barcodes for sainsbury's.

Why did I do this?

Because when doing my sainbury's bug bounty I needed working barcodes in incrementing orders to effectivly bruteforce the weights for the Mod-10 checkum algo. We manually tested there checkdigit to get the working barcodes we needed. For example we had:

```
915059319022437000000
915059319022437100000
915059319022437010000
915059319022437000010
```

These barcodes allowed us to see the impact of each digit on the checksum and using a simple bruteforcer we managed to find paterns. For example each digit for the price had a weight of 2,1,2,1. Given out bruteforcer and a hefty digital ocean bill we managed to reverse there checkdigit in just a couple weeks.

Why did I upload the barcodes?

Mainly because they have no use, without a correct way of checking checkdigits they are useless + most Uk retailers are moving over to digital ways of reductions.

