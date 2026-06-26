# Detailed AI Art Portfolio Framework Structure

## Section 1: Subject Matter (A)
What the image depicts - the core content and focus

1. **Primary Subject** :: Character, object, scene, or concept
2. **Perspective/Viewpoint** :: Angle, distance, framing
3. **Quantity/Number** :: Single, multiple, crowds, variations
4. **Action/Activity** :: What subjects are doing or state
5. **Details/Features** :: Specific attributes, characteristics
6. **Anatomy/Structure** :: Physical form, proportions, parts
7. **Expression/Mood** :: Emotional state, facial expressions
8. **Interaction/Relationship** :: How subjects relate to each other
9. **Narrative Context** :: Story element, role in larger scene

## Section 2: Style & Technique (B)
Artistic approach, medium, and rendering methods

1. **Artistic Movement** :: Historical or contemporary art movement
2. **Medium/Format** :: Physical or digital medium used
3. **Rendering Technique** :: How the image is created/appears
4. **Visual Texture** :: Surface quality and tactile feel
5. **Color Treatment** :: Overall color approach and palette
6. **Brushwork/Stroke** :: Mark-making and application method
7. **Lighting Style** :: Type and quality of illumination
8. **Composition Approach** :: Overall structural method
9. **Finishing Style** :: Final polish and presentation

## Section 3: Composition & Layout (C)
Visual arrangement, structure, and spatial organization

1. **Focal Point** :: Primary area of visual attention
2. **Rule Application** :: Composition rules used (rule of thirds, golden ratio, etc.)
3. **Balance/Weight** :: Visual weight distribution
4. **Depth/Layering** :: Foreground, middle ground, background
5. **Lines/Paths** :: Leading lines, geometric elements
6. **Symmetry/Asymmetry** :: Balance and pattern structure
7. **Framing Elements** :: Borders, vignettes, containers
8. **Negative Space** :: Empty or minimal areas
9. **Flow/Movement** :: Visual path through the image

## Section 4: Color & Lighting (D)
Chromatic elements and illumination characteristics

1. **Color Palette** :: Dominant and supporting colors
2. **Temperature** :: Warm, cool, or mixed color temperature
3. **Contrast Level** :: High, medium, low contrast
4. **Lighting Direction** :: Where light is coming from
5. **Light Quality** :: Hard, soft, diffused, etc.
6. **Shadow Treatment** :: How shadows are rendered
7. **Highlight Areas** :: Brightest parts and accents
8. **Atmospheric Effects** :: Mist, fog, haze, etc.
9. **Time of Day** :: Lighting that suggests specific times

## Section 5: Context & Setting (E)
Environment, background, and situational elements

1. **Location/Place** :: Geographic or constructed setting
2. **Architecture** :: Buildings, structures, interiors
3. **Background Elements** :: Supporting environmental details
4. **Cultural Context** :: Time period, society, customs
5. **Season/Weather** :: Environmental conditions
6. **Scale/Size** :: Relative proportions and measurements
7. **Historical Period** :: Temporal setting
8. **Cultural/Social Setting** :: Societal context
9. **Narrative Environment** :: Story-relevant surroundings

## Section 6: Modifiers & Effects (F)
Enhancements, alterations, and special treatments

1. **Post-Processing Effects** :: Digital enhancements and filters
2. **Texture Overlays** :: Additional surface qualities
3. **Atmospheric Conditions** :: Weather, environmental effects
4. **Optical Effects** :: Lens flares, bokeh, aberrations
5. **Digital Manipulation** :: Composite elements, alterations
6. **Artistic Filters** :: Stylized treatments
7. **Special FX** :: Fantasy or sci-fi elements
8. **Mood Enhancers** :: Elements that intensify emotion
9. **Stylization Level** :: Degree of artistic interpretation

## Section 7: Technical Parameters (G)
Platform-specific settings and technical considerations

1. **Resolution/Quality** :: Output clarity and detail level
2. **Aspect Ratio** :: Proportions of the image
3. **Platform Tags** :: NightCafe, Midjourney, DALL-E specific terms
4. **Model Version** :: Specific AI model identifiers
5. **Parameter Settings** :: Technical controls (--ar, --v, --style, etc.)
6. **Negative Prompts** :: Elements to exclude or avoid
7. **Generation Count** :: Number of variations or attempts
8. **Refinement Steps** :: Additional processing passes
9. **Output Format** :: File type and specifications

## Section 8: Quality & Presentation (H)
Output characteristics and final presentation considerations

1. **Professional Quality** :: Commercial or artistic standard
2. **Presentation Format** :: How it will be displayed
3. **Audience Target** :: Intended viewers or market
4. **Purpose/Use** :: Intended application or function
5. **Style Consistency** :: Cohesion with other works
6. **Portfolio Position** :: Where it fits in your body of work
7. **Series Relationship** :: Connection to other pieces
8. **Exhibition Context** :: How it might be shown
9. **Completion Status** :: Final, draft, or work-in-progress

## Weight System Reference
- ::0.1 = Minimal presence
- ::0.2 = Very low presence
- ::0.3 = Low presence
- ::0.4 = Below moderate presence
- ::0.5 = Moderate presence
- ::0.6 = Above moderate presence
- ::0.7 = High presence
- ::0.8 = Very high presence
- ::0.9 = Extremely high presence
- ::1.0 = Maximum presence (default when no weight specified)

## Nested Prompt Structure
Main Prompt :: [Nested Element :: Weight | Another Nested Element :: Weight] :: Main Section Weight

Example:
"Cyberpunk cityscape :: [flying cars :: 0.7 | neon signs :: 0.9] :: 0.8 futuristic architecture :: 1.0"