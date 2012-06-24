%include	/usr/lib/rpm/macros.perl
Summary:	Games-WordFind perl module
Summary(pl):	Modu� perla Games-WordFind
Name:		perl-Games-WordFind
Version:	0.02
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Games/Games-WordFind-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games-WordFind module simply provides a class which can be used to
generate WordFind type puzzles.

%description -l pl
Games-WordFind udost�pnia klas� do generowania puzzli.

%prep
%setup -q -n Games-WordFind-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Games/WordFind
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz examples

%{perl_sitelib}/Games/WordFind.pm
%{perl_sitelib}/auto/Games/WordFind/autosplit.ix

%{perl_sitearch}/auto/Games/WordFind

%{_mandir}/man3/*
