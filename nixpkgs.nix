let
  rev = "692517bf851f2d8d999f0ad50f53fa1d2dd5c8f9";
  sha256 = "";
in
import (fetchTarball {
  inherit sha256;
  url = "https://github.com/NixOS/nixpkgs/archive/${rev}.tar.gz";
})
