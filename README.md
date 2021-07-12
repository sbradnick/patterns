```
#
# [20210712] Initial attempt at a WSL (package) pattern.
#
```

```
git clone -b wsl https://github.com/sbradnick/patterns.git
cd SPEC
```

Build with:
```
rpmbuild --target x86_64 -bb patterns-wsl.spec
````

Verify with:
```
zypper search --type pattern wsl
zypper info --type pattern --recommends wsl
```
