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

Install with:
```
sudo zypper in --recommends ~/rpmbuild/RPMS/x86_64/patterns-wsl-wsl-20210712-0.x86_64.rpm
```

Verify with:
```
zypper search --type pattern wsl
zypper info --type pattern --recommends wsl
```

Info on variables:
```
$ rpm --eval %{_sysconfdir}
/etc

$ rpm --eval %{buildroot}
/home/scott/rpmbuild/BUILDROOT/%{NAME}-%{VERSION}-%{RELEASE}.x86_64
```
