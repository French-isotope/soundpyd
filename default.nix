let pkgs = import ./nixpkgs.nix {};
  pythonEnv = pkgs.python310.withPackages(p : [p.pygame p.configparser]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}
