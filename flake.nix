{
  description = "Python + Pygame + VSCode + Tabby dev environment";

  inputs = {
    nixos-config.url = "github:BerndDonner/NixOS-Config";
    nixpkgs.follows = "nixos-config/nixpkgs";
  };

  outputs = { self, nixpkgs, nixos-config, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
        overlays = [
          nixos-config.overlays.unstable
          nixos-config.overlays.pygame-avx2
        ];
      };

      pythonDev = import (nixos-config + "/lib/python-develop.nix");
    in
    {
      devShells.${system}.default = pythonDev {
        inherit pkgs;
        inputs = { inherit nixos-config nixpkgs; };
        checkInputs = [ "nixos-config" ];
        symbol = "🐍";
        pythonVersion = pkgs.python3;

        extraPackages = with pkgs; [
          python3Packages.pygame-avx2
          python3Packages.debugpy
          python3Packages.black
          python3Packages.isort
          vscode                      # proprietäre VSCode-Version
          tabby-agent                 # CLI für lokalen Tabby-Server/Proxy
        ];

        message = "🐍 VSCode + Tabby + Python development shell ready";
      };
    };
}
