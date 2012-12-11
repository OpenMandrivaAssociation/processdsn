Summary:	Process DSN notifications, record them in a database
Name:		processdsn
Version:	1.0.0
Release:	2
License:	Apache License
Group:		System/Servers
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel

%description
The DSN processor processes delivery status notifications, and stores the
results in a SQL database via the APR DBD interface.

%prep

%setup -q

%build
autoreconf -fi
export LIBS="`apr-1-config --link-ld` `apu-1-config --link-ld`"
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_bindir}/processdsn
%{_mandir}/man1/processdsn.1*



%changelog
* Sun Apr 10 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2011.0
+ Revision: 652246
- import processdsn


* Sun Apr 10 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2010.2
- initial Mandriva release

