Name:           perl-libwww-perl
Version:        5.836
Release:        0
License:        GPL-2.0+ or Artistic
Summary:        A Perl interface to the World-Wide Web
Url:            http://search.cpan.org/dist/libwww-perl/
Group:          Development/Libraries
Source0:        libwww-perl-%{version}.tar.gz
Source1001: 	perl-libwww-perl.manifest
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(URI)
Requires:       perl(Compress::Zlib)
Requires:       perl-HTML-Parser >= 3.33
BuildArch:      noarch

%description
The libwww-perl collection is a set of Perl modules which provides a
simple and consistent application programming interface to the
World-Wide Web.  The main focus of the library is to provide classes
and functions that allow you to write WWW clients. The library also
contain modules that are of more general use and even classes that
help you implement simple HTTP servers.

%prep
%setup -q -n libwww-perl-%{version}
cp %{SOURCE1001} .

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
