%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Games-WordFind perl module
Summary(pl):	Modu³ perla Games-WordFind
Name:		perl-Games-WordFind
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Games/Games-WordFind-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Games-WordFind module simply provides a class which can be used to generate 
WordFind type puzzles.

%description -l pl
Games-WordFind udostêpnia klasê do generowania puzzli.

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
