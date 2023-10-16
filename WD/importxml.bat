cd C:\Program Files\AspenTech\AeBRS
wdbulkloadtool -w localhost -i01 "C:\p4\WD_Web\WD\data\WD XML\01 aspen wd booths bulk load mvt.xml"
wdbulkloadtool -w localhost -i02 "C:\p4\WD_Web\WD\data\WD XML\02 aspen wd scales bulk load mvt.xml"
wdbulkloadtool -w localhost -i04 "C:\p4\WD_Web\WD\data\WD XML\04 aspen wd material bulk load mvt.xml"
wdbulkloadtool -w localhost -i05 "C:\p4\WD_Web\WD\data\WD XML\05 aspen wd inventory bulk load mvt.xml"
wdbulkloadtool -w localhost -i06 "C:\p4\WD_Web\WD\data\WD XML\06 aspen wd bom exception bulk load mvt.xml"
wdbulkloadtool -w localhost -i07 "C:\p4\WD_Web\WD\data\WD XML\07 aspen wd orders bulk load mvt.xml"
wdbulkloadtool -w localhost -i08 "C:\p4\WD_Web\WD\data\WD XML\08 aspen wd campaign bulk load mvt.xml"
sign.cmd
