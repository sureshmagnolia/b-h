import os

def build_html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bentham and Hooker Classification - Print Ready</title>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    :root {
        --color-dicot: #8b0000;
        --color-gymno: #00008b;
        --color-mono: #d35400;
        
        --color-poly: #2980b9;
        --color-gamo: #27ae60;
        --color-monochlamy: #8e44ad;
        
        --color-thala-bg: #ebf5fb;
        --color-disci-bg: #fef9e7;
        --color-calyci-bg: #e8f8f5;
        
        --color-inferae-bg: #e9f7ef;
        --color-hetero-bg: #ebdef0;
        --color-bicar-bg: #f5eef8;

        --color-curve-bg: #f4ecf7;
        
        --color-mono-bg1: #fbeee6;
        --color-mono-bg2: #fdf2e9;
    }

    body {
        font-family: 'Open Sans', sans-serif;
        margin: 0;
        padding: 0;
        background-color: #d5d8dc;
        color: #333;
        font-size: 11px;
    }

    @media print {
        @page { size: A3 landscape; margin: 8mm; }
        body { background-color: #fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        .main-container { box-shadow: none; max-width: 100%; margin: 0; border: none; }
        .no-print { display: none; }
        .grid-container { background: #fff !important; padding: 0 !important; gap: 6px !important; }
    }

    .main-container {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 1680px;
        margin: 10px auto;
        background: #fff;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        border-radius: 6px;
        overflow: hidden;
    }

    .header-main {
        background-color: #1a252f;
        color: white;
        text-align: center;
        padding: 8px;
        font-family: 'Merriweather', serif;
        font-size: 18px;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-bottom: 2px solid #34495e;
    }
    
    .super-class-header {
        background-color: #2c3e50;
        color: #f1c40f;
        text-align: center;
        padding: 6px;
        font-weight: 700;
        font-size: 15px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid #34495e;
    }

    .grid-container {
        display: grid;
        grid-template-columns: 3.2fr 0.8fr 1fr;
        background: #e5e8e8;
        padding: 8px;
        gap: 8px;
        align-items: start;
    }

    /* --- LEVEL 1: Top Level Cards --- */
    .top-level-card {
        background-color: #ffffff;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .top-level-header {
        color: white;
        text-align: center;
        padding: 6px;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
    }
    .top-level-desc {
        font-size: 9.5px;
        font-weight: 400;
        margin-top: 2px;
        text-transform: none;
        opacity: 0.9;
    }

    /* --- LEVEL 2: Subclass Cards --- */
    .dicot-content {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        background: #f4f6f7;
        padding: 6px;
        gap: 6px;
        flex: 1;
    }
    .subclass-card {
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        border: 1px solid #dcdde1;
    }
    .subclass-header {
        color: white;
        text-align: center;
        padding: 6px;
        font-weight: 600;
        font-size: 11px;
    }
    .subclass-body {
        padding: 4px;
        display: flex;
        flex-direction: column;
        background: #f8f9f9;
        flex: 1;
    }

    /* --- LEVEL 3: Series Card --- */
    .series-block {
        display: flex;
        flex-direction: row;
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        border: 1px solid #d5dbdb;
        margin-bottom: 6px;
    }
    .series-left {
        flex: 0 0 25px;
        background-color: rgba(0,0,0,0.04);
        border-right: 1px solid #e5e8e8;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 6px 2px;
    }
    .series-title-vertical {
        writing-mode: vertical-rl;
        transform: rotate(180deg);
        font-weight: 700;
        font-size: 10px;
        color: #2c3e50;
        letter-spacing: 1px;
        text-align: center;
    }
    .series-content {
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 4px;
        background-color: #ffffff;
    }

    /* --- LEVEL 4: Order Card --- */
    .order-row {
        display: flex;
        background-color: #fbfcfc;
        border-radius: 3px;
        border: 1px solid #eaeded;
        margin-bottom: 4px;
    }
    .order-row:last-child { margin-bottom: 0; }
    
    .order-left {
        flex: 0 0 35%;
        padding: 4px;
        border-right: 1px dashed #d5dbdb;
        background-color: #fdfdfd;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    
    .order-title {
        font-weight: 700;
        color: white;
        font-size: 10px;
        text-transform: uppercase;
        padding: 3px 6px;
        border-radius: 3px;
        display: inline-block;
    }

    .order-desc {
        font-size: 8.5px;
        color: #555;
        background-color: #f4f6f7;
        border: 1px solid #eaeded;
        border-radius: 2px;
        padding: 3px 4px;
        margin-top: 4px;
        line-height: 1.1;
    }

    .families-right {
        flex: 1;
        padding: 4px;
        display: flex;
        flex-direction: column;
        gap: 4px;
        justify-content: center;
    }

    /* --- LEVEL 5 & 6: Family Card & Inner Description Box --- */
    .family-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 3px;
        padding: 4px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .family-card-title {
        font-weight: 700;
        color: #1a252f;
        font-size: 10px;
    }
    .family-card-desc {
        font-size: 8.5px;
        color: #555;
        background-color: #f9fbfc;
        border: 1px solid #e5e8e8;
        border-radius: 2px;
        padding: 3px 4px;
        margin-top: 2px;
        line-height: 1.1;
    }
    
    /* Series Specific Tints */
    .bg-thala .series-left { background-color: var(--color-thala-bg); }
    .bg-disci .series-left { background-color: var(--color-disci-bg); }
    .bg-calyci .series-left { background-color: var(--color-calyci-bg); }
    .bg-inferae .series-left { background-color: var(--color-inferae-bg); }
    .bg-hetero .series-left { background-color: var(--color-hetero-bg); }
    .bg-bicar .series-left { background-color: var(--color-bicar-bg); }
    .bg-curve .series-left { background-color: var(--color-curve-bg); }

    /* Gymnosperm & Monocot styling */
    .gymno-content { 
        padding: 6px; 
        display: flex; 
        flex-direction: column; 
        gap: 6px; 
        background: #f8f9f9;
        flex: 1;
    }
    .gymno-card {
        background: #ffffff;
        padding: 6px;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        border: 1px solid #d5dbdb;
    }
    .gymno-title { font-weight: 700; font-size: 11px; color: white; padding: 3px 6px; border-radius: 3px; display: inline-block; text-transform: uppercase;}
    .gymno-desc { 
        font-size: 8.5px; 
        color: #555; 
        background-color: #f9fbfc;
        border: 1px solid #eaeded;
        border-radius: 2px;
        padding: 3px;
        margin-top: 4px;
        line-height: 1.1;
    }
    
    .mono-content { 
        display: flex; 
        flex-direction: column; 
        background: #f8f9f9; 
        padding: 6px;
        gap: 6px;
        flex: 1;
    }
    
    .mono-series-card {
        display: flex;
        background-color: #fbfcfc;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        border: 1px solid #eaeded;
    }
    .mono-left { 
        flex: 0 0 35%; 
        padding: 6px; 
        border-right: 1px dashed #d5dbdb; 
        background-color: #fdfdfd;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .mono-left-title {
        font-weight: 700; 
        color: white; 
        font-size: 10px;
        padding: 3px 6px;
        border-radius: 3px;
        display: inline-block;
    }
    .mono-right { 
        flex: 1; 
        padding: 4px; 
        display: flex; 
        flex-direction: column; 
        gap: 4px; 
        justify-content: center;
        background-color: #ffffff;
    }

</style>
</head>
<body>

<div class="no-print" style="text-align: center; margin-bottom: 5px;">
    <button onclick="window.print()" style="padding: 8px 16px; font-size: 14px; cursor: pointer; background: #2c3e50; color: white; border: none; border-radius: 4px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">🖨️ Print Chart</button>
</div>

<div class="main-container">
    <div class="header-main">
        Bentham and Hooker's Classification
        <div style="font-size: 11px; font-weight: 400; font-family: 'Open Sans', sans-serif; letter-spacing: 0; margin-top: 2px; text-transform: none;">
            For MSc Botany Syllabus - University of Calicut
        </div>
    </div>
    
    <div class="super-class-header">
        PHANEROGAMS
    </div>
    
    <div class="grid-container">
        <!-- DICOTYLEDONS CARD -->
        <div class="top-level-card" style="border-top: 4px solid var(--color-dicot);">
            <div class="top-level-header" style="background-color: var(--color-dicot);">
                DICOTYLEDONS
                <div class="top-level-desc">Two cotyledons, open vascular bundles, reticulate venation</div>
            </div>
            
            <div class="dicot-content">
                <!-- POLYPETALAE CARD -->
                <div class="subclass-card">
                    <div class="subclass-header" style="background-color: var(--color-poly);">
                        POLYPETALAE
                        <div class="top-level-desc" style="font-size: 8.5px;">Two distinct whorls of perianth; corolla free</div>
                    </div>
                    
                    <div class="subclass-body">
                        <!-- THALAMIFLORAE -->
                        <div class="series-block bg-thala">
                            <div class="series-left"><div class="series-title-vertical">THALAMIFLORAE</div></div>
                            <div class="series-content">
                                <!-- RANALES -->
                                <div class="order-row" style="border-left: 4px solid #3498db;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #3498db;">RANALES</div>
                                        <div class="order-desc">Bisexual/Unisexual, hypogynous, many free stamens/carpels</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #3498db;">
                                            <div class="family-card-title">1. RANUNCULACEAE</div>
                                            <div class="family-card-desc">Herbs with radially symmetrical flowers, numerous free parts spirally arranged. Alternate, dissected leaves.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #3498db;">
                                            <div class="family-card-title">2. MAGNOLIACEAE</div>
                                            <div class="family-card-desc">Trees/shrubs, aromatic. Bisexual, actinomorphic, 9-12 spirally arranged perianth segments.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #3498db;">
                                            <div class="family-card-title">3. MENISPERMACEAE</div>
                                            <div class="family-card-desc">Dioecious woody vines. Unisexual flowers, 3-8 sepals, no petals.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #3498db;">
                                            <div class="family-card-title">4. NYMPHAEACEAE</div>
                                            <div class="family-card-desc">Aquatic herbs, rhizomatous stems, peltate floating leaves. Large showy flowers.</div>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- PARIETALES -->
                                <div class="order-row" style="border-left: 4px solid #16a085;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #16a085;">PARIETALES</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="order-title" style="margin-top: 1px; background-color: #16a085; font-size: 9px; padding: 2px 4px;">POLYGALYNEAE</div>
                                        <div class="order-desc" style="margin-top: 0; margin-bottom: 2px;">Herbs/shrubs, exstipulate leaves, bilocular ovary</div>
                                        <div class="family-card" style="border-left: 3px solid #16a085;">
                                            <div class="family-card-title">5. POLYGALACEAE</div>
                                            <div class="family-card-desc">Alternate/whorled leaves, 5 sepals (3 petal-like). 8 stamens united in tube.</div>
                                        </div>
                                        
                                        <div class="order-title" style="margin-top: 4px; background-color: #16a085; font-size: 9px; padding: 2px 4px;">CARYOPHYLLINIAE</div>
                                        <div class="order-desc" style="margin-top: 0; margin-bottom: 2px;">Regular flowers, free central placentation</div>
                                        <div class="family-card" style="border-left: 3px solid #16a085;">
                                            <div class="family-card-title">6. CARYOPHYLLACEAE</div>
                                            <div class="family-card-desc">Opposite entire leaves, clawed petals, 2-5 united carpels.</div>
                                        </div>
                                    </div>
                                </div>
 
                                <!-- GUTTIFERALES -->
                                <div class="order-row" style="border-left: 4px solid #e67e22;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #e67e22;">GUTTIFERALES</div>
                                        <div class="order-desc">Radial flowers, numerous stamens, superior ovary</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #e67e22;">
                                            <div class="family-card-title">7. GUTTIFERAE (Clusiaceae)</div>
                                            <div class="family-card-desc">Trees/shrubs, shiny leaves. 4-8 colorful wrinkled petals, clustered stamens.</div>
                                        </div>
                                    </div>
                                </div>
 
                                <!-- MALVALES -->
                                <div class="order-row" style="border-left: 4px solid #f1c40f;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #f1c40f;">MALVALES</div>
                                        <div class="order-desc">Palmately veined stipulate leaves, stamens united in tube</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #f1c40f;">
                                            <div class="family-card-title">8. STERCULIACEAE</div>
                                            <div class="family-card-desc">Alternate simple stipulate leaves. Bisexual, twice as many stamens as petals.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
 
                        <!-- DISCIFLORAE -->
                        <div class="series-block bg-disci">
                            <div class="series-left"><div class="series-title-vertical">DISCIFLORAE</div></div>
                            <div class="series-content">
                                <!-- GERANIALES -->
                                <div class="order-row" style="border-left: 4px solid #2ecc71;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #2ecc71;">GERANIALES</div>
                                        <div class="order-desc">10 stamens, 5-carpellate superior ovary, nectary disc</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #2ecc71;">
                                            <div class="family-card-title">9. MELIACEAE</div>
                                            <div class="family-card-desc">Trees/climbers, pinnate leaves without stipules. Stamens often fused.</div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="order-row" style="border-left: 4px solid #1abc9c;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #1abc9c;">OLACALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
                                <div class="order-row" style="border-left: 4px solid #34495e;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #34495e;">CELASTRALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
 
                                <!-- SAPINDALES -->
                                <div class="order-row" style="border-left: 4px solid #f39c12;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #f39c12;">SAPINDALES</div>
                                        <div class="order-desc">Compound leaves, variable stamens</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #f39c12;">
                                            <div class="family-card-title">10. SAPINDACEAE</div>
                                            <div class="family-card-desc">Compound leaves, unisexual/bisexual. Fruit a capsule/schizocarp (winged).</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
 
                        <!-- CALYCIFLORAE -->
                        <div class="series-block bg-calyci">
                            <div class="series-left"><div class="series-title-vertical">CALYCIFLORAE</div></div>
                            <div class="series-content">
                                <!-- ROSALES -->
                                <div class="order-row" style="border-left: 4px solid #e74c3c;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #e74c3c;">ROSALES</div>
                                        <div class="order-desc">Stipulate leaves, perigynous, apocarpous</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #e74c3c;">
                                            <div class="family-card-title">11. ROSACEAE</div>
                                            <div class="family-card-desc">Actinomorphic with hypanthium. Fruit achene, follicle, drupe, or pome.</div>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- MYRTALES -->
                                <div class="order-row" style="border-left: 4px solid #c0392b;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #c0392b;">MYRTALES</div>
                                        <div class="order-desc">Aromatic leaves, epigynous, 2-5 fused carpels</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #c0392b;">
                                            <div class="family-card-title">12. RHIZOPHOREAE</div>
                                            <div class="family-card-desc">Mangroves, opposite stipulate leaves. Inferior syncarpous ovary.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #c0392b;">
                                            <div class="family-card-title">13. MELASTOMACEAE</div>
                                            <div class="family-card-desc">Nodes often thickened, hypanthium present. Poricidal anthers.</div>
                                        </div>
                                    </div>
                                </div>
 
                                <!-- FICOIDALES -->
                                <div class="order-row" style="border-left: 4px solid #9b59b6;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #9b59b6;">FICOIDALES</div>
                                        <div class="order-desc">Simple leaves, superior syncarpous ovary</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #9b59b6;">
                                            <div class="family-card-title">14. AIZOACEAE</div>
                                            <div class="family-card-desc">Succulent herbs/shrubs. Petals absent or few. Parietal placentation.</div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="order-row" style="border-left: 4px solid #8e44ad;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #8e44ad;">PASSIFLORALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
                                <div class="order-row" style="border-left: 4px solid #2980b9;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #2980b9;">UMBELLALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
 
                <!-- GAMOPETALAE CARD -->
                <div class="subclass-card">
                    <div class="subclass-header" style="background-color: var(--color-gamo);">
                        GAMOPETALAE
                        <div class="top-level-desc" style="font-size: 8.5px;">Two distinct whorls of perianth; corolla fused</div>
                    </div>
 
                    <div class="subclass-body">
                        <!-- INFERAE -->
                        <div class="series-block bg-inferae">
                            <div class="series-left"><div class="series-title-vertical">INFERAE</div></div>
                            <div class="series-content">
                                <!-- RUBIALES -->
                                <div class="order-row" style="border-left: 4px solid #27ae60;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #27ae60;">RUBIALES</div>
                                        <div class="order-desc">Opposite stipulate leaves, tubular epigynous, bicarpellate</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #27ae60;">
                                            <div class="family-card-title">15. RUBIACEAE</div>
                                            <div class="family-card-desc">Interpetiolar stipules. Calyx fused, corolla tubular. Inferior ovary.</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="order-row" style="border-left: 4px solid #16a085;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #16a085;">ASTERALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
                                <div class="order-row" style="border-left: 4px solid #f39c12;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #f39c12;">CAMPANALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
                            </div>
                        </div>
 
                        <!-- HETEROMERAE -->
                        <div class="series-block bg-hetero">
                            <div class="series-left"><div class="series-title-vertical">HETEROMERAE</div></div>
                            <div class="series-content">
                                <div class="order-row" style="border-left: 4px solid #8e44ad;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #8e44ad;">ERICALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
                                <div class="order-row" style="border-left: 4px solid #2980b9;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #2980b9;">PRIMULALES</div>
                                    </div>
                                    <div class="families-right"></div>
                                </div>
                                <!-- EBENALES -->
                                <div class="order-row" style="border-left: 4px solid #c0392b;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #c0392b;">EBENALES</div>
                                        <div class="order-desc">Simple entire leaves, superior compound ovary</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #c0392b;">
                                            <div class="family-card-title">16. SAPOTACEAE</div>
                                            <div class="family-card-desc">Trees/shrubs with milky latex. Corolla sympetalous.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
 
                        <!-- BICARPELLATAE -->
                        <div class="series-block bg-bicar">
                            <div class="series-left"><div class="series-title-vertical">BICARPELLATAE</div></div>
                            <div class="series-content">
                                <!-- GENTIANALES -->
                                <div class="order-row" style="border-left: 4px solid #f39c12;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #f39c12;">GENTIANALES</div>
                                        <div class="order-desc">Simple stipulate leaves, superior bicarpellate ovary</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #f39c12;">
                                            <div class="family-card-title">17. GENTIANACEAE</div>
                                            <div class="family-card-desc">Opposite/whorled leaves. Bitter glycosides. Parietal placentation.</div>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- POLEMONEALES -->
                                <div class="order-row" style="border-left: 4px solid #e67e22;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #e67e22;">POLEMONEALES</div>
                                        <div class="order-desc">Exstipulate leaves, tubular corolla, epipetalous stamens</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #e67e22;">
                                            <div class="family-card-title">18. BORAGINACEAE</div>
                                            <div class="family-card-desc">Alternate basal leaves. Deeply 4-lobed ovary, fruit a schizocarp.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #e67e22;">
                                            <div class="family-card-title">19. CONVOLVULACEAE</div>
                                            <div class="family-card-desc">Herbs/climbers. Corolla sympetalous, ovary superior bicarpellate.</div>
                                        </div>
                                    </div>
                                </div>
 
                                <!-- PERSONALES -->
                                <div class="order-row" style="border-left: 4px solid #d35400;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #d35400;">PERSONALES</div>
                                        <div class="order-desc">Zygomorphic flowers, didynamous stamens</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #d35400;">
                                            <div class="family-card-title">20. SCROPHULARIACEAE</div>
                                            <div class="family-card-desc">Zygomorphic, numerous ovules per locule on axile placentation.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #d35400;">
                                            <div class="family-card-title">21. PEDALIACEAE</div>
                                            <div class="family-card-desc">Viscid pubescent leaves. Corolla bilabiate. Capsule with hooks/spines.</div>
                                        </div>
                                    </div>
                                </div>
 
                                <!-- LAMIALES -->
                                <div class="order-row" style="border-left: 4px solid #8e44ad;">
                                    <div class="order-left">
                                        <div class="order-title" style="background-color: #8e44ad;">LAMIALES</div>
                                        <div class="order-desc">Irregular zygomorphic flowers, reduced stamens</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #8e44ad;">
                                            <div class="family-card-title">22. VERBENACEAE</div>
                                            <div class="family-card-desc">Quadrangular stems. Terminal panicles, corolla tubular.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
 
                <!-- MONOCHLAMYDEAE CARD -->
                <div class="subclass-card">
                    <div class="subclass-header" style="background-color: var(--color-monochlamy);">
                        MONOCHLAMYDEAE
                        <div class="top-level-desc" style="font-size: 8.5px;">Only one non-essential whorl or absent</div>
                    </div>
 
                    <div class="subclass-body">
                        <!-- CURVEMBRYAE -->
                        <div class="series-block bg-curve">
                            <div class="series-left"><div class="series-title-vertical">CURVEMBRYAE</div></div>
                            <div class="series-content">
                                <div class="order-row" style="border-left: 4px solid #9b59b6;">
                                    <div class="order-left" style="display:flex; align-items:flex-start;">
                                        <div class="order-desc" style="margin:0;">Single ovule, embryo coiled around endosperm</div>
                                    </div>
                                    <div class="families-right">
                                        <div class="family-card" style="border-left: 3px solid #9b59b6;">
                                            <div class="family-card-title">23. NYCTAGINACEAE</div>
                                            <div class="family-card-desc">Perianth of 3-5 tepals. Basal placentation, fruit achene/utricle.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
 
                        <div class="order-row" style="border-left: 4px solid #3498db;">
                            <div class="order-left" style="flex: 1; border-right: none;">
                                <div class="order-title" style="background-color: #3498db;">MULTIOVULATAE AQUATICAE</div>
                            </div>
                        </div>
                        <div class="order-row" style="border-left: 4px solid #e74c3c;">
                            <div class="order-left" style="flex: 1; border-right: none;">
                                <div class="order-title" style="background-color: #e74c3c;">MULTIOVULATAE TERROSTRIS</div>
                            </div>
                        </div>
                        <div class="order-row" style="border-left: 4px solid #2ecc71;">
                            <div class="order-left" style="flex: 1; border-right: none;">
                                <div class="order-title" style="background-color: #2ecc71;">MICROEMBRAE</div>
                            </div>
                        </div>
                        <div class="order-row" style="border-left: 4px solid #9b59b6;">
                            <div class="order-left" style="flex: 1; border-right: none;">
                                <div class="order-title" style="background-color: #9b59b6;">DAPHNALES</div>
                            </div>
                        </div>
                        <div class="order-row" style="border-left: 4px solid #e67e22;">
                            <div class="order-left" style="flex: 1; border-right: none;">
                                <div class="order-title" style="background-color: #e67e22;">ACHLAMYDOSPOREAE</div>
                            </div>
                        </div>
                        
                        <!-- UNISEXUALES -->
                        <div class="series-block">
                            <div class="series-left" style="background-color:#fcf3cf;"><div class="series-title-vertical">UNISEXUALES</div></div>
                            <div class="series-content">
                                <div class="order-row" style="border-left: 4px solid #f1c40f;">
                                    <div class="families-right" style="padding-left: 0;">
                                        <div class="family-card" style="border-left: 3px solid #f1c40f;">
                                            <div class="family-card-title">24. EUPHORBIACEAE</div>
                                            <div class="family-card-desc">Milky sap. Unisexual, apetalous. 3-loculed ovary.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #f1c40f;">
                                            <div class="family-card-title">25. URTICACEAE</div>
                                            <div class="family-card-desc">Stinging hairs. Perianth 4-5 lobed, fruit achene or drupe.</div>
                                        </div>
                                        <div class="family-card" style="border-left: 3px solid #f1c40f;">
                                            <div class="family-card-title">26. CASUARINACEAE</div>
                                            <div class="family-card-desc">Whorled branchlets like pine needles. Woody cone fruit.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="order-row" style="border-left: 4px solid #34495e;">
                            <div class="order-left" style="flex: 1; border-right: none;">
                                <div class="order-title" style="background-color: #34495e;">ORDINES ANOMALI</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
 
        <!-- GYMNOSPERMS CARD -->
        <div class="top-level-card" style="border-top: 4px solid var(--color-gymno);">
            <div class="top-level-header" style="background-color: var(--color-gymno);">
                GYMNOSPERMS
                <div class="top-level-desc">Naked seeded Plants without Vessels</div>
            </div>
            <div class="gymno-content">
                <div class="gymno-card" style="border-left-color: #3498db;">
                    <div class="gymno-title" style="background-color: #3498db;">Gnetales</div>
                    <div class="gymno-desc">No vessel elements in their wood. Compound cones with fleshy seeds.</div>
                </div>
                <div class="gymno-card" style="border-left-color: #2ecc71;">
                    <div class="gymno-title" style="background-color: #2ecc71;">Coniferales (Conifers)</div>
                    <div class="gymno-desc">Cone-bearing nature and their needle-like or scale-like leaves.</div>
                </div>
                <div class="gymno-card" style="border-left-color: #e74c3c;">
                    <div class="gymno-title" style="background-color: #e74c3c;">Cycadales (Cycads)</div>
                    <div class="gymno-desc">Produce conspicuously large cones front like leaves.</div>
                </div>
            </div>
        </div>
 
        <!-- MONOCOTYLEDONS CARD -->
        <div class="top-level-card" style="border-top: 4px solid var(--color-mono);">
            <div class="top-level-header" style="background-color: var(--color-mono);">
                MONOCOTYLEDONS
                <div class="top-level-desc">One cotyledon, closed vascular bundles, parallel venation, trimerous flowers</div>
            </div>
            <div class="mono-content">
                <!-- MICROSPERMAE -->
                <div class="mono-series-card" style="border-left: 4px solid #d35400;">
                    <div class="mono-left" style="background-color: var(--color-hetero-bg);">
                        <div class="mono-left-title" style="background-color: #d35400;">MICROSPERMAE</div>
                        <div class="order-desc" style="margin-top: 3px;">Inferior ovary; minute seeds</div>
                    </div>
                    <div class="mono-right">
                        <div class="family-card" style="border-left: 3px solid #d35400;">
                            <div class="family-card-title">27. ORCHIDACEAE</div>
                            <div class="family-card-desc">Perennial epiphytic herbs. 3-petaled zygomorphic flowers. Pollinia.</div>
                        </div>
                    </div>
                </div>
                
                <!-- EPIGYNAE -->
                <div class="mono-series-card" style="border-left: 4px solid #e67e22;">
                    <div class="mono-left" style="background-color: var(--color-mono-bg1);">
                        <div class="mono-left-title" style="background-color: #e67e22;">EPIGYNAE</div>
                        <div class="order-desc" style="margin-top: 3px;">Inferior ovary; large seeds with copious endosperm</div>
                    </div>
                    <div class="mono-right">
                        <div class="family-card" style="border-left: 3px solid #e67e22;">
                            <div class="family-card-title">28. ZINGIBERACEAE</div>
                            <div class="family-card-desc">Aromatic rhizomes, distichous leaves, spike inflorescence.</div>
                        </div>
                        <div class="family-card" style="border-left: 3px solid #e67e22;">
                            <div class="family-card-title">29. AMARYLLIDACEAE</div>
                            <div class="family-card-desc">Bulbous herbs, actinomorphic, inferior ovary.</div>
                        </div>
                    </div>
                </div>
 
                <!-- CORONARIAE -->
                <div class="mono-series-card" style="border-left: 4px solid #f39c12;">
                    <div class="mono-left" style="background-color: #d5f5e3;">
                        <div class="mono-left-title" style="background-color: #f39c12;">CORONARIAE</div>
                        <div class="order-desc" style="margin-top: 3px;">Perianth petaloid; superior ovary</div>
                    </div>
                    <div class="mono-right">
                        <div class="family-card" style="border-left: 3px solid #f39c12;">
                            <div class="family-card-title">30. LILIACEAE</div>
                            <div class="family-card-desc">Bulbs/corms, parallel-veined leaves, actinomorphic flowers.</div>
                        </div>
                        <div class="family-card" style="border-left: 3px solid #f39c12;">
                            <div class="family-card-title">31. COMMELINACEAE</div>
                            <div class="family-card-desc">Flattened leaf sheaths, zygomorphic (2 large, 3 small petals).</div>
                        </div>
                    </div>
                </div>
 
                <div class="mono-series-card" style="border-left: 4px solid #8e44ad;">
                    <div class="mono-left" style="background-color: #fdfdfd; flex: 1; border-right: none;">
                        <div class="mono-left-title" style="background-color: #8e44ad;">CALYCINAE</div>
                    </div>
                </div>
 
                <!-- NUDIFLORAE -->
                <div class="mono-series-card" style="border-left: 4px solid #c0392b;">
                    <div class="mono-left" style="background-color: var(--color-curve-bg);">
                        <div class="mono-left-title" style="background-color: #c0392b;">NUDIFLORAE</div>
                        <div class="order-desc" style="margin-top: 3px;">Perianth absent or minute scales</div>
                    </div>
                    <div class="mono-right">
                        <div class="family-card" style="border-left: 3px solid #c0392b;">
                            <div class="family-card-title">32. ARACEAE</div>
                            <div class="family-card-desc">Spadix inflorescence, simple leaves, unisexual flowers.</div>
                        </div>
                    </div>
                </div>
 
                <div class="mono-series-card" style="border-left: 4px solid #2980b9;">
                    <div class="mono-left" style="background-color: #fdfdfd; flex: 1; border-right: none;">
                        <div class="mono-left-title" style="background-color: #2980b9;">APOCARPAE</div>
                    </div>
                </div>
 
                <!-- GLUMACEAE -->
                <div class="mono-series-card" style="border-left: 4px solid #f1c40f;">
                    <div class="mono-left" style="background-color: #fcf3cf;">
                        <div class="mono-left-title" style="background-color: #f1c40f; color: #333;">GLUMACEAE</div>
                        <div class="order-desc" style="margin-top: 3px;">Scaly/glumaceous perianth; one-ovuled ovary</div>
                    </div>
                    <div class="mono-right">
                        <div class="family-card" style="border-left: 3px solid #f1c40f;">
                            <div class="family-card-title">33. CYPERACEAE</div>
                            <div class="family-card-desc">Grass-like, solid stems, 3-ranked leaves, spikelets.</div>
                        </div>
                        <div class="family-card" style="border-left: 3px solid #f1c40f;">
                            <div class="family-card-title">34. GRAMINEAE</div>
                            <div class="family-card-desc">Hollow stems, 2-ranked leaves, caryopsis fruit.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 20px; background: #2c3e50; color: white; border-top: 2px solid #1a252f;">
        <div style="font-size: 10px; opacity: 0.8;">
            Prepared by
        </div>
        <div style="text-align: right; font-size: 11px; font-weight: bold;">
            Dr. Suresh V, Department of Botany, Government Victoria College, Palakkad, Kerala
        </div>
    </div>
</div>

</body>
</html>"""
    with open(r"C:\Users\sures\.gemini\antigravity-ide\scratch\bentham_hooker_final_print.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Success")

build_html()
