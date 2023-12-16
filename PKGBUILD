pkgname=randsay
pkgver=1.0
pkgrel=1
pkgdesc="Generates a random quote, and makes a random cowfile say it."
arch=('any')
url="https://github.com/mario0fan-cooldude/randsay"
license=('GPL')
depends=('cowsay' 'fortune-mod')

source=("randsay.py::https://raw.githubusercontent.com/mario0fan-cooldude/randsay/main/randsay.py")

sha256sums=('put_the_calculated_checksum_here')

noextract=("$pkgname-$pkgver")

package() {
  install -Dm755 "$srcdir/randsay.py" "$pkgdir/usr/bin/randsay.py"
}
