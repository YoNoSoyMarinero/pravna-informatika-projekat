class StopWords:
    header_starts: list[str] = ["U IME CRNE GORE"]
    judgemnt_starts: list[str] = ["P R E S U D U"]
    guilty_starts: list[str] = ["KRIV JE", "KRIVJE", "K R I V J E", "kriv je", "krivje", "K r i v j e"]
    judging_to_starts: list[str] = ["O S U D J U J E", 'O S U Đ U J E', 'O S U Đ  U J E', 'O S U D J U J E', 'O S U Đ  U J E', 'O S U DJ U J E', 'O s u đ  u j e', 'OSUDJUJE', 'O s uđu j e', 'USLOVNU OSUDU']
    explnation_starts: list[str] = ["O b r a z l ože nj e", 'O b r a z l ože n j e', 'Obrazloženje', 'O b r a z o l ože n j e']